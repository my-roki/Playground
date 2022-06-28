import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")  # 가로x세로


def info():
    msgbox.showinfo("alerting", "alert!!!")

def warn():
    msgbox.showinfo("warning", "warning!!!")

def error():
    msgbox.showinfo("error", "bad error!!!")

def okcancel():
    msgbox.askokcancel("choose", "ok or cancel?")

def retrycancel():
    msgbox.askretrycancel("retry", "try again")

def yesno():
    msgbox.askyesno("yes or no", "choose yes or no")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="yes/no/cancel")
    # "네" : True
    # "아니오" : False
    # "취소" : None
    # print(f"response : {response}")

    if response is True:
        print("예")
    elif response is False:
        print("아니요")
    elif response is None:
        print("취소")
    else:
        print("Error")

Button(root, command=info, text="infomation").pack()
Button(root, command=warn, text="warning").pack()
Button(root, command=error, text="error").pack()

Button(root, command=okcancel, text="ok/cancel").pack()
Button(root, command=retrycancel, text="retry/cancel").pack()
Button(root, command=yesno, text="yes/no").pack()
Button(root, command=yesnocancel, text="yes/no/cancel").pack()

root.mainloop()