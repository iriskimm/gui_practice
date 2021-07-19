from tkinter import *

root = Tk() 
root.title("Nado GUI")
root.geometry('640x480+300+100') # 가로 * 세로 + x좌표 + y좌표

listbox = Listbox(root, selectmode='extended', height=0) # selectmode='extended' means we can click on multiple items
# listbox = Listbox(root, selectmode='extended', height=3) # have to scroll down to see items beyond index 3

listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤에 항목을 삭제
    # listbox.delete(0) # 맨 앞 항목을 삭제

    # 갯수 확인
    # print('리스트에는', listbox.size(), '개가 있어요')

    # 항목 확인 (시작 idx, 끝 idx)
    print('1번째부터 3번째까지의 항목:' , listbox.get(0,2))

    # 사용자가 선택(클릭)한 항목 확인
    print('Selected itmes:', listbox.curselection()) # current selection; prints the index

btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop()



