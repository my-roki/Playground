from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")

txt = Text(root, width=30, height=5)
txt.insert(END, "You can write anything!")
txt.pack()

e = Entry(root, width=30)  # 한 줄만 입력 가능한 text widget
e.insert(0, "You can write only one line")
e.pack()

def btncmd():
    # 내용 출력
    print(txt.get("1.0", END))  # 1: 1번째 line, 0: 0번째 column
    print(e.get()) 

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()