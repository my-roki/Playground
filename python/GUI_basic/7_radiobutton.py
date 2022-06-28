from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")

Label(root, text="Please select food").pack()

food_var = IntVar()  # int형식으로 값을 저장
btn_food1 = Radiobutton(root, text="pizza", value=1, variable=food_var)
btn_food1.select()  # 자동 선택 처리(기본값)
btn_food2 = Radiobutton(root, text="chicken", value=2, variable=food_var)
btn_food3 = Radiobutton(root, text="hamburger", value=3, variable=food_var)
btn_food4 = Radiobutton(root, text="bibimbob", value=4, variable=food_var)

btn_food1.pack()
btn_food2.pack()
btn_food3.pack()
btn_food4.pack()

Label(root, text="Please select drink").pack()

drink_var = StringVar()  # string형식으로 값을 저장
btn_drink1 = Radiobutton(root, text="coke", value="coke", variable=drink_var)
btn_drink1.select()  # 자동 선택 처리(기본값)
btn_drink2 = Radiobutton(root, text="sprite", value="sprite", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(food_var.get())  # food 중 선택된 라디오 항목의 값(value)을 출력
    print(drink_var.get())  # drink 중 선택된 라디오 항목의 값(value)을 출력

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()