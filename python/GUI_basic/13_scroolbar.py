from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")  # 가로x세로

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

# 스크롤바에도 리스트박스와 맵핑해줘야 함
scrollbar.config(command=listbox.yview) 

root.mainloop()