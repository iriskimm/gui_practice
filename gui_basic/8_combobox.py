import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry('640x480+300+100') # 가로 * 세로 + x좌표 + y좌표 

values = [str(i)+'일' for i in range(1, 32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values) # height는 목록에 몇개가 동시에 보여지는지 정함
combobox.pack()
combobox.set('카드 결제일') # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state='readonly') # 읽기 전용, 사용자가 직접 입력 불가
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()


def btncmd():
    print(combobox.get()) # 선택된 값을 출력
    print(readonly_combobox.get())

btn = Button(root, text='선택', command=btncmd)
btn.pack()

root.mainloop()



