from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")  # 가로x세로

# btn1 = Button(root, text="button1")
# btn2 = Button(root, text="button2")

# # btn1.pack()
# # btn2.pack()
# # btn1.pack(side="left")
# # btn2.pack(side="right")

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)


# 텐키 버튼 디자인 하기
# 기능키 줄
btn_cal = Button(root, text="cal", width=5, height=2)
btn_cam = Button(root, text="cam", width=5, height=2)
btn_sc = Button(root, text="sc", width=5, height=2)
btn_lock = Button(root, text="lock", width=5, height=2)

btn_cal.grid(row=0, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_cam.grid(row=0, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_sc.grid(row=0, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_lock.grid(row=0, column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=1, column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7키 줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

btn_7.grid(row=2, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=2, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

# 4키 줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)

btn_4.grid(row=3, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky=N+E+W+S, padx=3, pady=3)

# 1키 줄
btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3)

# 0키 줄
btn_0 = Button(root, text="0", width=5, height=2)
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5, column=2, sticky=N+E+W+S, padx=3, pady=3)

root.mainloop()