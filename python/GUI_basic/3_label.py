from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")

label1 = Label(root, text="Hello World")
label1.pack()

photo = PhotoImage(file="GUI_basic/check.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="Bye World")

    global photo2  # Garbage Collection : 불필요한 메모리 공간 해제. 글로벌변수 설정
    photo2 = PhotoImage(file="GUI_basic/img_x.png")
    label2.config(image=photo2)

btn1 = Button(root, text="click", command=change)
btn1.pack()

root.mainloop()