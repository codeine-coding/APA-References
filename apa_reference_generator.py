from tkinter import *
from classes import *

primary = '#222b34'
text_color = '#ffffff'
separators = '#662d91'
btn_primary = '#662d91'
btn_active = '#501f75'


def create_separator():
    separator = Frame(height=2, bd=1, relief=FLAT, bg=separators)
    separator.pack(fill=X, padx=5, pady=5)


class ApaReference(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('APA References')
        self.master.iconbitmap('favicon.ico')
        self.master.resizable(width=False, height=False)
        self.master.config(bg=primary)

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

    def create_article_section(self):
        article_frame = Frame(self.master, padx=5, pady=5, bg=primary)
        Label(article_frame, text='Article Title:', bg=primary, fg=text_color).grid(row=0, sticky=W)
        Entry(article_frame, width=46, textvariable=self.article_title).grid(row=1, column=0, sticky=W)
        article_frame.pack(anchor=W)

    def create_contributors_section(self):
        contributors_frame = Frame(self.master, padx=5, pady=5, bg=primary)
        Label(contributors_frame, text='Contributors:', font=('', 11, 'bold'),
              bg=primary, fg=text_color).grid(row=0, columnspan=3, sticky=W)
        # first name
        Label(contributors_frame, text='First Name', bg=primary, fg=text_color).grid(row=1, sticky=W)
        Entry(contributors_frame, width=20, textvariable=self.contributor_first_name).grid(row=2, column=0, sticky=W)
        # middle name
        Label(contributors_frame, text='MI', bg=primary, fg=text_color).grid(row=1, column=1, sticky=W)
        Entry(contributors_frame, width=5, textvariable=self.contributor_middle_name).grid(row=2, column=1, sticky=W)
        # last name
        Label(contributors_frame, text='Last Name', bg=primary, fg=text_color).grid(row=1, column=2, sticky=W)
        Entry(contributors_frame, width=20, textvariable=self.contributor_last_name).grid(row=2, column=2, sticky=W)
        contributors_frame.pack(anchor=W)

        # Add Contributor Button
        add_contributor_btn = Frame(self.master, padx=5, pady=5, bg=primary)
        Button(add_contributor_btn, text='+ Add another contributor', bg=btn_primary, activebackground=btn_active,
               activeforeground=text_color, fg=text_color, relief=FLAT, command=self.add_contributor).pack(anchor=E)
        add_contributor_btn.pack(anchor=E)

    def create_journal_info_section(self):
        journal_pub_info_frame = Frame(self.master, padx=5, pady=5, bg=primary)
        journal_pub_info_label = Label(text='Journal Publication Info', padx=5, bg=primary, fg=text_color)

        # Journal title
        journal_title_frame = Frame(journal_pub_info_frame, bg=primary)
        Label(journal_title_frame, text="Journal Title:", bg=primary, fg=text_color).grid(row=0, column=0, sticky=W)
        Entry(journal_title_frame, width=46, textvariable=self.journal_title).grid(row=1, column=0, sticky=W)
        journal_title_frame.pack(anchor=W)

        # Additional Info
        Label(journal_pub_info_frame, text="Additional Info", pady=10, bg=primary, fg=text_color).pack(anchor=W)
        journal_advanced_info_frame = Frame(journal_pub_info_frame, pady=5, bg=primary)

        Label(journal_advanced_info_frame, text="Volume", bg=primary, fg=text_color).grid(row=2, column=0, sticky=W)
        Entry(journal_advanced_info_frame, width=12, textvariable=self.journal_volume).grid(row=3, column=0, sticky=W)

        Label(journal_advanced_info_frame, text='Issue', bg=primary, fg=text_color).grid(row=2, column=1, sticky=W)
        Entry(journal_advanced_info_frame, width=12, textvariable=self.journal_issue).grid(row=3, column=1, sticky=W)

        journal_advanced_info_frame.pack(anchor=W)

        # Year Published
        year_published_frame = Frame(journal_pub_info_frame, pady=5, bg=primary)

        Label(year_published_frame, text='Year Published:', bg=primary, fg=text_color).grid(row=0, sticky=W)
        Entry(year_published_frame, width=12, textvariable=self.year_published).grid(row=1, column=0, sticky=W)
        year_published_frame.pack(anchor=W)
        # Pages - Start, End
        pub_pages_frame = Frame(journal_pub_info_frame, pady=5, bg=primary)
        Label(pub_pages_frame, text='Pages:', bg=primary, fg=text_color).grid(row=0, columnspan=2, sticky=W)

        Label(pub_pages_frame, text='Start', bg=primary, fg=text_color).grid(row=1, column=0, sticky=W)
        Entry(pub_pages_frame, width=5, textvariable=self.pages_start).grid(row=2, column=0, sticky=W)

        Label(pub_pages_frame, text='End', bg=primary, fg=text_color).grid(row=1, column=1, sticky=W)
        Entry(pub_pages_frame, width=5, textvariable=self.pages_end).grid(row=2, column=1, sticky=W)
        pub_pages_frame.pack(anchor=W)
        # DOI
        pub_doi_frame = Frame(journal_pub_info_frame, bg=primary)

        Label(pub_doi_frame, text='DOI/Website:', bg=primary, fg=text_color).grid(row=0, sticky=W)
        Entry(pub_doi_frame, width=46, textvariable=self.doi).grid(row=1, column=0, sticky=W)
        pub_doi_frame.pack(anchor=W)

        journal_pub_info_label.pack(anchor=W)
        journal_pub_info_frame.pack(anchor=W)

        # Generate Button
        generate_frame = Frame(self.master, padx=5, pady=5, bg=primary)
        gen_button = Button(generate_frame, text='Generate', bg=btn_primary, activebackground=btn_active,
                            activeforeground=text_color, fg=text_color, relief=FLAT, command=self.generate)
        gen_button.pack(expand=0, fill=X)
        generate_frame.pack(expand=0, fill=X)

    def build_apa_generator(self):
        # Title Label
        Label(self.master, text='APA References Generator', font=('', 14, 'bold'),
              padx=5, bg=primary, fg=text_color).pack()
        create_separator()
        # Article Frame
        self.create_article_section()
        # Contributors Frame
        self.create_contributors_section()
        create_separator()
        # Journal Info
        self.create_journal_info_section()

    def add_contributor(self):
        Contributor(self.contributor_first_name.get(), self.contributor_middle_name.get(),
                    self.contributor_last_name.get())
        self.contributor_first_name.set('')
        self.contributor_middle_name.set('')
        self.contributor_last_name.set('')

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


ApaReference().mainloop()
