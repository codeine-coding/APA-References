from tkinter import *
from classes import *


def create_separator():
    separator = Frame(height=2, bd=1, relief=SUNKEN)
    separator.pack(fill=X, padx=5, pady=5)


class ApaReference:
    def __init__(self, master):
        self.master = master
        master.title('APA References')
        master.iconbitmap('favicon.ico')
        master.resizable(width=False, height=False)

        # Title Label
        Label(master, text='APA References Generator', font=('', 14, 'bold'), padx=5).pack()
        create_separator()
        # Article Frame
        self.article_frame = Frame(master, padx=5, pady=5)
        self.article_title = StringVar()
        self.article_title_label = Label(self.article_frame, text='Article Title:')
        self.article_title_label.grid(row=0, sticky=W)
        self.article_title_entry = Entry(self.article_frame, width=45, textvariable=self.article_title)
        self.article_title_entry.grid(row=1, column=0, sticky=W)
        self.article_frame.pack(anchor=W)

        # Contributors Frame
        self.c_first_name = StringVar()
        self.c_middle_name = StringVar()
        self.c_last_name = StringVar()
        self.c_suffix = StringVar()
        self.contributors_frame = Frame(master, padx=5, pady=5)
        self.contributors_label = Label(self.contributors_frame,
                                        text='Contributors:',
                                        font=('', 11, 'bold')
                                        ).grid(row=0, columnspan=3, sticky=W)
        # first name
        self.first_name_label = Label(self.contributors_frame, text='First Name').grid(row=1, sticky=W)
        self.contributors_first_name = Entry(self.contributors_frame, width=20,
                                             textvariable=self.c_first_name)
        self.contributors_first_name.grid(row=2, column=0, sticky=W)
        # middle name
        self.first_middle_label = Label(self.contributors_frame, text='MI').grid(row=1, column=1, sticky=W)
        self.contributors_middle_name = Entry(self.contributors_frame, width=5,
                                              textvariable=self.c_middle_name)
        self.contributors_middle_name.grid(row=2, column=1, sticky=W)
        # last name
        self.first_middle_label = Label(self.contributors_frame, text='Last Name').grid(row=1, column=2, sticky=W)
        self.contributors_middle_name = Entry(self.contributors_frame, width=20,
                                              textvariable=self.c_last_name)
        self.contributors_middle_name.grid(row=2, column=2, sticky=W)
        self.contributors_frame.pack(anchor=W)

        # Add Contributor Button
        self.add_contributor_btn = Frame(master, padx=5, pady=5)
        Button(self.add_contributor_btn, text='+ Add another contributor', command=self.add_contributor).pack(anchor=E)
        self.add_contributor_btn.pack(anchor=E)

        create_separator()

        # Journal Publication Info
        self.journal_pub_info_frame = Frame(master, padx=5, pady=5)
        self.journal_pub_info_label = Label(text='Journal Publication Info', padx=5)

        # TODO Journal title
        self.journal_title = StringVar()
        self.journal_title_frame = Frame(self.journal_pub_info_frame)
        Label(self.journal_title_frame, text="Journal Title:").grid(row=0, column=0, sticky=W)
        self.journal_title = Entry(self.journal_title_frame, width=45, textvariable=self.journal_title)
        self.journal_title.grid(row=1, column=0, sticky=W)
        self.journal_title_frame.pack(anchor=W)
        # Additional Info
        Label(self.journal_pub_info_frame, text="Additional Info", pady=10).pack(anchor=W)
        self.journal_advanced_info_frame = Frame(self.journal_pub_info_frame, pady=5)

        self.journal_volume = StringVar()
        Label(self.journal_advanced_info_frame, text="Volume").grid(row=2, column=0, sticky=W)
        self.journal_volume = Entry(self.journal_advanced_info_frame, width=12, textvariable=self.journal_volume)
        self.journal_volume.grid(row=3, column=0, sticky=W)

        self.journal_issue = StringVar()
        Label(self.journal_advanced_info_frame, text='Issue').grid(row=2, column=1, sticky=W)
        self.journal_issue = Entry(self.journal_advanced_info_frame, width=12, textvariable=self.journal_issue)
        self.journal_issue.grid(row=3, column=1, sticky=W)

        self.journal_advanced_info_frame.pack(anchor=W)
        # Year Published
        self.year_published_frame = Frame(self.journal_pub_info_frame, pady=5)

        self.year_published = StringVar()
        self.year_published_label = Label(self.year_published_frame, text='Year Published:').grid(row=0, sticky=W)
        self.year_published_entry = Entry(self.year_published_frame, width=12, textvariable=self.year_published).grid(
            row=1, column=0, sticky=W)
        self.year_published_frame.pack(anchor=W)
        # Pages - Start, End
        self.pub_pages_frame = Frame(self.journal_pub_info_frame, pady=5)
        self.pages_label = Label(self.pub_pages_frame, text='Pages:').grid(row=0, columnspan=2, sticky=W)

        self.pages_start = StringVar()
        self.pages_start_label = Label(self.pub_pages_frame, text='Start').grid(row=1, column=0, sticky=W)
        self.pages_start_entry = Entry(self.pub_pages_frame, width=5, textvariable=self.pages_start).grid(row=2,
                                                                                                          column=0,
                                                                                                          sticky=W)
        self.pages_end = StringVar()
        self.pages_start_label = Label(self.pub_pages_frame, text='End').grid(row=1, column=1, sticky=W)
        self.pages_end_entry = Entry(self.pub_pages_frame, width=5, textvariable=self.pages_end).grid(row=2, column=1,
                                                                                                      sticky=W)
        self.pub_pages_frame.pack(anchor=W)
        # DOI
        self.pub_DOI_frame = Frame(self.journal_pub_info_frame)
        self.doi = StringVar()
        self.DOI_label = Label(self.pub_DOI_frame, text='DOI/Website:').grid(row=0, sticky=W)
        self.DOI_entry = Entry(self.pub_DOI_frame, width=45, textvariable=self.doi).grid(row=1, column=0, sticky=W)
        self.pub_DOI_frame.pack(anchor=W)

        self.journal_pub_info_label.pack(anchor=W)
        self.journal_pub_info_frame.pack(anchor=W)

        # Generate Button
        self.generate_frame = Frame(master, padx=5, pady=5)
        self.gen_button = Button(self.generate_frame, text='Generate', command=self.generate)
        self.gen_button.pack(expand=0, fill=X)
        self.generate_frame.pack(expand=0, fill=X)

    def add_contributor(self):
        Contributor(self.c_first_name.get(), self.c_middle_name.get(), self.c_last_name.get())
        self.c_first_name.set('')
        self.c_middle_name.set('')
        self.c_last_name.set('')

    def generate(self):
        contributors = sorted(Contributor.contributors)

        if len(contributors) == 1:
            authors = contributors[0]
        elif len(contributors) == 2:
            authors = ', & '.join(contributors)
        elif 3 <= len(contributors) <= 7:
            authors = (', '.join(contributors[0:-1]) + ', & {}'.format(contributors[-1]))
        elif len(contributors) > 7:
            authors = (', '.join(contributors[0:6]) + ',...{}'.format(contributors[-1]))
        else:
            authors = ''

        journal = Journal(self.article_title.get(), self.journal_title.get(), self.year_published.get(),
                          self.pages_start.get(), self.pages_end.get(), self.journal_volume.get(),
                          self.journal_issue.get(), self.doi.get())

        reference = Reference(authors, journal.get_journal_entry())

        print(reference.get_reference())


root = Tk()
ApaReference(root)
root.mainloop()
