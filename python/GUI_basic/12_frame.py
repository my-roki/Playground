from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")  # 가로x세로

Label(root, text="select menu").pack(side="top")
Button(root, text="order").pack(side="bottom")

# 메뉴 프레임
frame_food = Frame(root, relief="solid", bd=1)
frame_food.pack(side="left", fill="both", expand=True)

Button(frame_food, text="pizza").pack()
Button(frame_food, text="chicken").pack()
Button(frame_food, text="hamburger").pack()
Button(frame_food, text="bibimbob").pack()

# 음료 프레임
frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="coke").pack()
Button(frame_drink, text="sprite").pack()

root.mainloop()