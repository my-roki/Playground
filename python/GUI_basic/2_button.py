from tkinter import *

root = Tk()
root.title("roki_GUI")

btn1 = Button(root, text="button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="button2")  # 공간(여백)을 확보(padding)
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="button33333333333333")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button44444444444")  # 가로,세로(고정) 길이 설정
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="button5")
btn5.pack()

photo = PhotoImage(file="GUI_basic/check.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("button is activated")

btn7 = Button(root, text="active button", command=btncmd)
btn7.pack()

root.mainloop()