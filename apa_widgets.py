from tkinter import *

primary = '#222b34'
text_color = '#ffffff'
separators = '#662d91'
btn_primary = '#662d91'
btn_active = '#501f75'


class Separator(Frame):
    """Creates Separator"""
    def __init__(self, master=None, **options):
        Frame.__init__(self, master, **options)
        self.config(height=2, bd=1, relief=FLAT, bg=separators)
        self.pack(fill=X, padx=5, pady=5)


class PrimaryButton(Button):
    """Create Primary styling for buttons"""
    def __init__(self, master, **options):
        Button.__init__(self, master, **options)
        self.config(bg=btn_primary, activebackground=btn_active,
                    activeforeground=text_color, fg=text_color, relief=FLAT,)


class PrimaryLabel(Label):
    """Create Primary styling for Labels"""
    def __init__(self, master, **options):
        Label.__init__(self, master, **options)
        self.config(bg=primary, fg=text_color)
