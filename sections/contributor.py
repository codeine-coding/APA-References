from tkinter import Entry, W, StringVar, Listbox, BOTH

from utils.apa_widgets import *


class ContributorSection(Section):
    def __init__(self, master, **options):
        Section.__init__(self, master, **options)

        self.contributor_first_name = StringVar()
        self.contributor_middle_name = StringVar()
        self.contributor_last_name = StringVar()

        contributors_frame = Section(self.master)
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


class ContributorListBox(Section):
    def __init__(self, master, **options):
        Section.__init__(self, master, **options)

        PrimaryLabel(self.master, text='Current Article Contributors').pack()
        self.contributor_listbox = Listbox(self.master)
        self.contributor_listbox.pack(fill=BOTH)