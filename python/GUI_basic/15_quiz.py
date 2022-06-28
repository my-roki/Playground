"""
Quiz) tkinter를 이용한 메모장 프로그램을 만들어보기

[GIU 조건]
1. title : 제목 없음 - windows 메모장
2. 메뉴 : 파일, 편집, 서식, 보기, 도움말
3. 실제 메뉴 구현 : 파일 메누 내에서 열기, 저장, 끝내기 3개만 처리
    3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
    3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
    3-3. 끝내기 : 프로그램 종료
4. 프로그램 시작 시 본문은 비워져있는 상태
5. 하단 status 바는 필요 없음
6. 프로그램 크기, 위치는 자유롭게 하되, 크기 조정이 가능해야 함
7. 본문 우측에 상하 스크롤 바 넣기
"""

from tkinter import *
import os

def open_file():
    if os.path.isfile('mynote.txt'):
        with open('mynote.txt', 'r', encoding='utf-8') as notepad:
            content = notepad.read()
            txt.delete("1.0", END)
            txt.insert(END, content)
        return 
    else:
        with open('mynote.txt', 'w', encoding='utf-8') as notepad:
            return


def save_file():
    content = txt.get("1.0", END)
    with open('mynote.txt', 'w', encoding='utf-8') as notepad:
        notepad.write(content)


root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")  # 가로x세로

frame = Frame(root)
frame.pack(expand=True, fill="both")

# 메뉴 : 파일, 편집, 서식, 보기, 도움말
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기(O)...", command=open_file)
menu_file.add_command(label="저장(S)", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기(X)", command=root.quit) 

menu.add_cascade(label="파일(F)", menu=menu_file)
menu.add_cascade(label="편집(E)")
menu.add_cascade(label="서식(O)")
menu.add_cascade(label="보기(V)")
menu.add_cascade(label="도움말(H)")

# 스크롤바
scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 텍스트 위젯
txt = Text(frame, width=10, height=10, yscrollcommand=scrollbar.set)
txt.pack(side="left", expand=True, fill="both")

scrollbar.config(command=txt.yview) 
root.config(menu=menu)
root.mainloop()