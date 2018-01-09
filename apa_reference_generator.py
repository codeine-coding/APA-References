from classes import *
from apa_widgets import *
import tkinter.filedialog


def save_as_docx():
    try:
        input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension='.docx',
                                                               filetypes=[
                                                                   ("Word Documents", '*.docx')
                                                               ])
        if input_file_name:
            Reference.create_word_doc(input_file_name)
    except PermissionError:
        print("File open elsewhere!")


class ApaReference(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('APA References')
        self.master.iconbitmap('favicon.ico')
        self.center_window()
        self.master.resizable(width=True, height=False)
        self.master.config(bg=primary)
        self.content_text = None
        self.contributor_listbox = None
        self.ref_listbox = None
        self.contributor_first_name_entry = None
        self.article_title_entry = None

        # Variables
        self.article_title = StringVar()
        self.contributor_first_name = StringVar()
        self.contributor_middle_name = StringVar()
        self.contributor_last_name = StringVar()
        self.journal_title = StringVar()
        self.journal_volume = StringVar()
        self.journal_issue = StringVar()
        self.year_published = StringVar()
        self.pages_start = StringVar()
        self.pages_end = StringVar()
        self.doi = StringVar()

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

    def create_contributors_section(self, parent):
        contributors_frame = Section(parent)
        PrimaryLabel(contributors_frame, text='Contributors:', font=('', 11, 'bold')).grid(row=0, columnspan=3,
                                                                                           sticky=W)
        # first name
        PrimaryLabel(contributors_frame, text='First Name').grid(row=1, sticky=W)
        self.contributor_first_name_entry = Entry(contributors_frame, width=20,
                                                  textvariable=self.contributor_first_name)
        self.contributor_first_name_entry.grid(row=2, column=0, sticky=W)
        # middle name
        PrimaryLabel(contributors_frame, text='MI').grid(row=1, column=1, sticky=W)
        Entry(contributors_frame, width=5, textvariable=self.contributor_middle_name).grid(row=2, column=1, sticky=W)
        # last name
        PrimaryLabel(contributors_frame, text='Last Name').grid(row=1, column=2, sticky=W)
        Entry(contributors_frame, width=20, textvariable=self.contributor_last_name).grid(row=2, column=2, sticky=W)
        contributors_frame.pack(anchor=W)

        # Add Contributor Button
        add_contributor_btn = Section(parent)
        PrimaryButton(add_contributor_btn, text='+ Add another contributor',
                      command=self.add_contributor).pack(anchor=E)
        add_contributor_btn.pack(anchor=E)

    def create_journal_info_section(self, parent):
        journal_pub_info_frame = Section(parent)
        journal_pub_info_label = Label(parent, text='Journal Publication Info', padx=5, bg=primary, fg=text_color)

        # Journal title
        journal_title_frame = Frame(journal_pub_info_frame, bg=primary)
        PrimaryLabel(journal_title_frame, text="Journal Title:").grid(row=0, column=0, sticky=W)
        Entry(journal_title_frame, width=46, textvariable=self.journal_title).grid(row=1, column=0, sticky=W)
        journal_title_frame.pack(anchor=W)

        # Additional Info
        PrimaryLabel(journal_pub_info_frame, text="Additional Info", pady=10).pack(anchor=W)
        journal_advanced_info_frame = Frame(journal_pub_info_frame, pady=5, bg=primary)

        PrimaryLabel(journal_advanced_info_frame, text="Volume").grid(row=2, column=0, sticky=W)
        Entry(journal_advanced_info_frame, width=12, textvariable=self.journal_volume).grid(row=3, column=0, sticky=W)

        PrimaryLabel(journal_advanced_info_frame, text='Issue').grid(row=2, column=1, sticky=W)
        Entry(journal_advanced_info_frame, width=12, textvariable=self.journal_issue).grid(row=3, column=1, sticky=W)

        journal_advanced_info_frame.pack(anchor=W)

        # Year Published
        year_published_frame = Frame(journal_pub_info_frame, pady=5, bg=primary)

        PrimaryLabel(year_published_frame, text='Year Published:').grid(row=0, sticky=W)
        Entry(year_published_frame, width=12, textvariable=self.year_published).grid(row=1, column=0, sticky=W)
        year_published_frame.pack(anchor=W)
        # Pages - Start, End
        pub_pages_frame = Frame(journal_pub_info_frame, pady=5, bg=primary)
        PrimaryLabel(pub_pages_frame, text='Pages:').grid(row=0, columnspan=2, sticky=W)

        PrimaryLabel(pub_pages_frame, text='Start').grid(row=1, column=0, sticky=W)
        Entry(pub_pages_frame, width=5, textvariable=self.pages_start).grid(row=2, column=0, sticky=W)

        PrimaryLabel(pub_pages_frame, text='End').grid(row=1, column=1, sticky=W)
        Entry(pub_pages_frame, width=5, textvariable=self.pages_end).grid(row=2, column=1, sticky=W)
        pub_pages_frame.pack(anchor=W)
        # DOI
        pub_doi_frame = Frame(journal_pub_info_frame, bg=primary)

        PrimaryLabel(pub_doi_frame, text='DOI/Website:').grid(row=0, sticky=W)
        Entry(pub_doi_frame, width=46, textvariable=self.doi).grid(row=1, column=0, sticky=W)
        pub_doi_frame.pack(anchor=W)

        journal_pub_info_label.pack(anchor=W)
        journal_pub_info_frame.pack(anchor=W)

        # Generate Button
        add_ref_frame = Section(parent)
        PrimaryButton(add_ref_frame, text='Add Reference', command=self.add_reference).pack(expand=0, fill=X)
        add_ref_frame.pack(expand=0, fill=X)
        generate_frame = Section(parent)
        gen_button = PrimaryButton(generate_frame, text='Generate',  command=self.generate)
        gen_button.pack(expand=0, fill=X)
        generate_frame.pack(expand=0, fill=X)

    def create_generated_reference_frame(self, parent):
        PrimaryLabel(parent, text='Generated References').pack(anchor=W)
        content_text_frame = Frame(parent)
        self.content_text = Text(content_text_frame)
        self.content_text.pack(expand='yes', fill='both', side=LEFT, anchor=NW)
        self.content_text.config(wrap='none', pady=5)

        scroll_bar_y = Scrollbar(content_text_frame)
        self.content_text.configure(yscrollcommand=scroll_bar_y.set)
        scroll_bar_y.config(command=self.content_text.yview)
        scroll_bar_y.pack(side=RIGHT, fill='y', anchor=E)
        content_text_frame.pack(expand='yes', fill='both')

        scroll_bar_x_frame = Frame(parent)
        scroll_bar_x = Scrollbar(scroll_bar_x_frame, orient=HORIZONTAL)
        self.content_text.configure(xscrollcommand=scroll_bar_x.set)
        scroll_bar_x.config(command=self.content_text.xview)
        scroll_bar_x.pack(side=BOTTOM, fill='x', anchor=SW)
        scroll_bar_x_frame.pack(fill='x')

        save_btn_frame = Frame(parent, bg=primary)
        save_btn_frame.grid_rowconfigure(0, pad=5)
        save_btn_frame.grid_columnconfigure(0, pad=5)
        PrimaryButton(save_btn_frame, text='Save as Text File', command=self.save_as_txt).grid(row=0, sticky=SW)
        PrimaryButton(save_btn_frame, text='Save as Word File',  command=save_as_docx).grid(row=0, column=1, sticky=SE)
        save_btn_frame.pack(anchor=SE)

    def create_contributor_listbox(self, parent):
        PrimaryLabel(parent, text='Current Article Contributors').pack()
        self.contributor_listbox = Listbox(parent)
        self.contributor_listbox.pack(fill=BOTH)

    def create_reference_listbox(self, parent):
        PrimaryLabel(parent, text='Current References').pack()
        self.ref_listbox = Listbox(parent)
        self.ref_listbox.pack(fill=BOTH)

    def build_apa_generator(self):
        # Title Label
        PrimaryLabel(self.master, text='APA References Generator', font=('', 14, 'bold'), padx=5).pack()
        Separator()
        details_frame = Frame(self.master, bg=primary)
        # Article Frame
        self.create_article_section(details_frame)
        # Contributors Frame
        self.create_contributors_section(details_frame)
        Separator(details_frame)
        # Journal Info
        self.create_journal_info_section(details_frame)
        details_frame.pack(side=LEFT)

        listbox_frame = Frame(self.master, padx=5, pady=5, bg=primary)
        self.create_contributor_listbox(listbox_frame)
        self.create_reference_listbox(listbox_frame)
        listbox_frame.pack(side=LEFT, anchor=N)

        content_text_frame = Frame(self.master, padx=5, pady=5, bg=primary)
        self.create_generated_reference_frame(content_text_frame)
        content_text_frame.pack(expand='yes', side=LEFT, anchor=NW, fill=BOTH)

    def save_as_txt(self):
        input_file_name = tkinter.filedialog.asksaveasfilename(defaultextension='.txt',
                                                               filetypes=[
                                                                   ("Text Documents", '*.txt')
                                                               ])
        if input_file_name:
            self.write_to_file(input_file_name)

    def write_to_file(self, filename):
        try:
            content = self.content_text.get(1.0, END)
            with open(filename, 'w') as the_file:
                the_file.write(content)
        except IOError:
            pass

    def update_contributor_list(self):
        contributors = sorted(Contributor.contributors)
        self.contributor_listbox.delete(0, END)
        for c in contributors:
            self.contributor_listbox.insert(END, c)

    def update_reference_list(self):
        references = Reference.get_sorted_references()
        self.ref_listbox.delete(0, END)
        for r in references:
            self.ref_listbox.insert(END, r.journal.article_title)

    def add_contributor(self):
        Contributor(self.contributor_first_name.get(), self.contributor_middle_name.get(),
                    self.contributor_last_name.get())
        self.update_contributor_list()

        # Reset contributor fields to empty
        vars_to_eval = ('contributor_first_name', 'contributor_middle_name', 'contributor_last_name')
        for v in vars_to_eval:
            eval('self.' + v).set('')

        self.contributor_first_name_entry.focus_set()

    def add_reference(self):
        authors = Contributor.get_contributors()

        journal = Journal(self.article_title.get(), self.journal_title.get(), self.year_published.get(),
                          self.pages_start.get(), self.pages_end.get(), self.journal_volume.get(),
                          self.journal_issue.get(), self.doi.get())

        Reference(authors, journal)

        # reset all reference entry fields to empty
        vars_to_eval = ('article_title', 'contributor_first_name', 'contributor_middle_name', 'contributor_last_name',
                        'journal_title', 'journal_volume', 'journal_issue', 'year_published', 'pages_start',
                        'pages_end', 'doi')
        for v in vars_to_eval:
            eval('self.' + v).set('')

        Contributor.contributors.clear()
        self.update_contributor_list()
        self.update_reference_list()
        self.article_title_entry.focus_set()

    def generate(self):
        self.content_text.delete(1.0, END)
        references = '\n\n'.join(sorted(Reference.formatted_references))
        self.content_text.insert(1.0, references)


ApaReference().mainloop()
