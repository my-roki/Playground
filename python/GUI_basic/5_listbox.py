from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "lemon")
listbox.insert(2, "grape")
listbox.insert(END, "banana")
listbox.insert(END, "melon")
listbox.pack()

def btncmd():
    # listbox.delete(0)  # 맨 앞 항목 삭제
    # print(f"{listbox.size()} fruit(s) in the list")  # 개수 확인
    # print(f"1~3 fruits : {listbox.get(0, 2)}")  # 항목 확인 get(시작항목, 끝항목)
    print(f"seleted friut : {listbox.curselection()}")  # 선택된 항목 확인, 위치로 출력

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()