import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1,32)]  # 1~31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.set("payment day")
combobox.pack()

# readonly(값 수정 불가)
readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
readonly_combobox.current(0)  # 0번쨰 인덱스값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get())  # 선택된 값 표시
    print(readonly_combobox.get())

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()