from tkinter import Listbox, BOTH

from apa_widgets import Section, PrimaryLabel


class ReferenceListSection(Section):
    def __init__(self, master, **options):
        Section.__init__(self, master, **options)

        PrimaryLabel(self.master, text='Current References').pack()
        self.ref_listbox = Listbox(self.master)
        self.ref_listbox.pack(fill=BOTH)
