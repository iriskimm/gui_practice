import tkinter.ttk as ttk
from tkinter import *

root = Tk() 
root.title("Image Combiner")

# file frame (add/delete files)
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text='Add file(s)')
btn_add_file.pack(side='left')

btn_delete_file = Button(file_frame, padx=5, pady=5, width=12, text='Delete file(s)')
btn_delete_file.pack(side='right')

# list frame
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)
scrollbar.config(command=list_file.yview)

# file path frame
path_frame = LabelFrame(root, text='File path')
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4) # adjusting height

btn_dest_path = Button(path_frame, text='Search', width=10)
btn_dest_path.pack(side='right', padx=5, pady=5)


# option frame
option_frame = LabelFrame(root, text='Option')
option_frame.pack(padx=5, pady=5, ipady=5)

# Option 1. width size 
lbl_width = Label(option_frame, text='Width:', width=8)
lbl_width.pack(side='left', pady=5)

opt_width = ['Original size', '1024', '800', '640']
cmb_width = ttk.Combobox(option_frame, state='readonly', values=opt_width, width=10)
cmb_width.current(0)
cmb_width.pack(side='left', padx=5, pady=5)


# Option 2. space size 
lbl_space = Label(option_frame, text='Space:', width=8)
lbl_space.pack(side='left', pady=5)

opt_space = ['None', 'Narrow', 'Normal', 'Wide']
cmb_space = ttk.Combobox(option_frame, state='readonly', values=opt_space, width=10)
cmb_space.current(0)
cmb_space.pack(side='left', padx=5, pady=5)

# Option 3. file format option 
lbl_format = Label(option_frame, text='Format:', width=8)
lbl_format.pack(side='left', pady=5)

opt_format = ['PNG', 'JPG', 'BMP']
cmb_format = ttk.Combobox(option_frame, state='readonly', values=opt_format, width=10)
cmb_format.current(0)
cmb_format.pack(side='left', padx=5, pady=5)


# progress bar
progress_frame = LabelFrame(root, text='Saving file ...')
progress_frame.pack(fill='x', padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar= ttk.Progressbar(progress_frame, maximum=100, variable=p_var)
progress_bar.pack(fill='x', padx=10, pady=10)


# run frame
run_frame = Frame(root)
run_frame.pack(fill='x', padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text='Close', width=12, command=root.quit)
btn_close.pack(side='right', padx=5, pady=5)

run_btn = Button(run_frame, padx=5, pady=5, text='Start', width=12)
run_btn.pack(side='right', padx=5, pady=5)


root.resizable(False, False) 
root.mainloop()



