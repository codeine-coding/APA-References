from tkinter import *
from apa_widgets import *
from models.contributor import Contributor
from models.journal import Journal
from models.reference import Reference
from sections.contributor import ContributorSection, ContributorListBox
from sections.journal import JournalSection
from sections.reference import ReferenceListSection
from utils import save_as_docx


class ApaReference(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('APA References')
        self.master.iconbitmap('favicon.ico')
        # self.center_window()
        self.master.resizable(width=True, height=False)
        self.master.config(bg=primary)
        self.contributor_lb = None
        self.ref_lb = None
        self.contributor_section = None
        self.journal_section = None
        self.article_title_entry = None

        # Variables
        self.article_title = StringVar()

        self.build_apa_generator()

    def center_window(self):
        w = 1155
        h = 600

        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = int((sw - w) / 2)
        y = int((sh - h) / 2)
        self.master.geometry(f'{w}x{h}+{x}+{y}')

    def create_article_section(self, parent):
        article_frame = Section(parent)
        PrimaryLabel(article_frame, text='Article Title:').grid(row=0, sticky=W)
        self.article_title_entry = Entry(article_frame, width=46, textvariable=self.article_title)
        self.article_title_entry.grid(row=1, column=0, sticky=W)
        article_frame.pack(anchor=W)

    def build_apa_generator(self):
        # Title Label
        PrimaryLabel(self.master, text='APA References Generator', font=('', 14, 'bold'), padx=5).pack()
        Separator()
        details_frame = Frame(self.master, bg=primary)

        # Article Frame
        self.create_article_section(details_frame)

        # Contributors Frame
        self.contributor_section = ContributorSection(master=details_frame)

        # Add Contributor Button
        add_contributor_btn = Section(details_frame)
        PrimaryButton(add_contributor_btn, text='+ Add another contributor',
                      command=self.add_contributor
                      ).pack(anchor=E)
        add_contributor_btn.pack(anchor=E)
        Separator(details_frame)

        # Journal Info
        self.journal_section = JournalSection(details_frame)
        # Generate Button
        add_ref_frame = Section(details_frame)
        PrimaryButton(add_ref_frame, text='Add Reference',
                      command=self.add_reference
                      ).pack(expand=0, fill=X)
        add_ref_frame.pack(expand=0, fill=X)

        details_frame.pack(side=LEFT)

        # List Frames
        listbox_frame = Frame(self.master, padx=5, pady=5, bg=primary)

        self.contributor_lb = ContributorListBox(listbox_frame)
        self.ref_lb = ReferenceListSection(listbox_frame)
        save_btn_frame = Frame(listbox_frame, bg=primary)
        save_btn_frame.grid_rowconfigure(0, pad=5)
        save_btn_frame.grid_columnconfigure(0)
        PrimaryButton(save_btn_frame, text='Save as Word File',  command=save_as_docx).grid(row=0, column=0, sticky=SW)
        save_btn_frame.pack(anchor=SE)
        listbox_frame.pack(side=LEFT, anchor=N)

    def update_contributor_list(self):
        contributors = sorted(Contributor.contributors)
        self.contributor_lb.contributor_listbox.delete(0, END)
        for c in contributors:
            self.contributor_lb.contributor_listbox.insert(END, c)

    def update_reference_list(self):
        rs = Reference.get_sorted_references()
        self.ref_lb.ref_listbox.delete(0, END)
        for r in rs:
            self.ref_lb.ref_listbox.insert(END, r.journal.article_title)

    def add_contributor(self):
        Contributor(self.contributor_section.contributor_first_name.get(),
                    self.contributor_section.contributor_middle_name.get(),
                    self.contributor_section.contributor_last_name.get())
        self.update_contributor_list()

        # Reset contributor fields to empty
        vars_to_eval = ('contributor_first_name', 'contributor_middle_name', 'contributor_last_name')
        for v in vars_to_eval:
            eval('self.contributor_section.' + v).set('')

            self.contributor_section.contributor_first_name_entry.focus_set()

    def add_reference(self):
        authors = Contributor.get_contributors()

        journal = Journal(self.article_title.get(), self.journal_section.journal_title.get(),
                          self.journal_section.year_published.get(), self.journal_section.pages_start.get(),
                          self.journal_section.pages_end.get(), self.journal_section.journal_volume.get(),
                          self.journal_section.journal_issue.get(), self.journal_section.doi.get())

        Reference(authors, journal)

        # reset all reference entry fields to empty
        self.article_title.set('')

        vars_to_eval = ('contributor_first_name', 'contributor_middle_name', 'contributor_last_name')
        for v in vars_to_eval:
            eval('self.contributor_section.' + v).set('')

        vars_to_eval = ('journal_title', 'journal_volume', 'journal_issue', 'year_published', 'pages_start',
                        'pages_end', 'doi')
        for v in vars_to_eval:
            eval('self.journal_section.' + v).set('')

        Contributor.contributors.clear()
        self.update_contributor_list()
        self.update_reference_list()
        self.article_title_entry.focus_set()


ApaReference().mainloop()
