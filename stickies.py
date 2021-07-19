import os
from tkinter import *

root = Tk()
root.title("Stickies")
root.geometry('400x250+300+100')

menu = Menu(root)

filename = 'mynote.txt'

def open_file():
    if os.path.isfile(filename):
        with open(filename, 'r', encoding='utf8') as file:
            txt.delete('1.0', END) # 본문 삭제 to reset
            txt.insert(END, file.read())

    # ------ another way to do it ------
    # lines = open('/Users/iriskim/Code/pythonworkspace/mynote.txt', 'r')
    # text_from_file = Label(root, text=lines.read())
    # text_from_file.pack()

def save_file():
    with open(filename, 'w', encoding='utf8') as file:
        file.write(txt.get('1.0', END))

# -------------- Menu 'File' --------------
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='Open...', command=open_file)
menu_file.add_command(label='Save', command=save_file)
menu_file.add_separator()
menu_file.add_command(label='Close', command=root.quit)

menu.add_cascade(label='File', menu=menu_file)

# -------------- Menu 'Edit' --------------
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label='Undo')
menu_edit.add_command(label='Redo')
menu_edit.add_separator()
menu_edit.add_command(label='Cut')
menu_edit.add_command(label='Copy')
menu_edit.add_command(label='Paste')

menu.add_cascade(label='Edit', menu=menu_edit)

# -------------- Menu 'Font' --------------
menu_font = Menu(menu, tearoff=0)
menu_font.add_command(label='Bold')
menu_font.add_command(label='Underline')
menu_font.add_command(label='Italic')
menu_edit.add_separator()
menu_font.add_command(label='Show Colours')

menu.add_cascade(label='Font', menu=menu_font)

# -------------- Menu 'Help' --------------
menu_font.add_command(label='Stickies Help')
menu.add_cascade(label='Help', menu=menu_font)

# scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')


# text on file
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side='left', fill='both', expand=True)

scrollbar.config(command=txt.yview)


# ---------------------------------
txt.config(bg="#FADA5E")

root.config(menu=menu)
root.mainloop()