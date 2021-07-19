import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI") 
root.geometry('640x480+300+100') # 가로 * 세로 + x좌표 + y좌표


frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill=Y)

# set이 없으면 스크롤을 내려도 다시 올라옴
# height: 한번에 몇개 보이는지
listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand = scrollbar.set)
for i in range(1, 32): # 1 ~ 31 일
    listbox.insert(END, str(i) + '일') # 1일, 2일, ...
listbox.pack(side='left')

scrollbar.config(command=listbox.yview) # scrollbar 랑 listbox를 묶음


root.mainloop()



