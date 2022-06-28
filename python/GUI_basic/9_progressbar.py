import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")

# # progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10)
# progressbar.pack()

# def btncmd():
#     progressbar.stop()  # 작동중지

# btn = Button(root, text="stop", command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar.pack()

def btncmd():
    for i in range(1,101):
        time.sleep(0.1)

        p_var2.set(i)
        progressbar.update()
        print(p_var2.get())
        
        if i == 100:
            print("done!")

btn = Button(root, text="start", command=btncmd)
btn.pack()

 





root.mainloop()