from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")

chkvar1 = IntVar()  # chkvar에 int형으로 값을 저장한다
chkbox1 = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar1)
# chkbox1.select()  # 자동 선택 처리
# chkbox1.deselect()  # 자동 해제 처리
chkbox1.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(f"chkbox1: {chkvar1.get()}")  # 0: deselect, 1: select
    print(f"chkbox2: {chkvar2.get()}")
    print()

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()