from tkinter import (
    Entry,
    StringVar,
    W
)
from utils.apa_widgets import *


class JournalSection(Section):
    def __init__(self, master, **options):
        Section.__init__(self, master, **options)

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

        journal_pub_info_frame = Section(self.master)
        journal_pub_info_label = Label(self.master, text='Journal Publication Info', padx=5, bg=primary, fg=text_color)

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
