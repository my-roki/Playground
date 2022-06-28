from tkinter import *

root = Tk()
root.title("roki_GUI")
root.geometry("640x480")

def creat_new_file():
    print("creat new file")


menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)

menu_file.add_command(label="New File", command=creat_new_file)
menu_file.add_command(label="New Windows")
menu_file.add_separator()
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")  # 비활성화
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit) 

menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴
menu.add_cascade(label="Edit")

# Language 메뉴(radio button으로 택1)
menu_language = Menu(menu, tearoff=0)

menu_language.add_radiobutton(label="Python")
menu_language.add_radiobutton(label="Java")
menu_language.add_radiobutton(label="C++")

menu.add_cascade(label="Language", menu=menu_language)

# View 메뉴(select button으로 다중 택)
menu_view = Menu(menu, tearoff=0)

menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="Show Breadcrumbs")

menu.add_cascade(label="View", menu=menu_view)


root.config(menu=menu)
root.mainloop()