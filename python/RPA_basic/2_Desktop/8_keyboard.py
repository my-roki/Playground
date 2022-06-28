import pyautogui
notepad = pyautogui.getWindowsWithTitle("new 1 - Notepad++")[0]
notepad.activate()

pyautogui.write("Hello world, ")
pyautogui.write("Hello Pycharm", interval=0.25)
pyautogui.write("\n")

pyautogui.write(["t", "e", "s", "t", "left", "left", "right", "l", "a", "delete", "enter"], interval=0.25)
# https://automatetheboringstuff.com/2e/chapter20/ 
# 위 사이트에서 단축키에 대한 정보를 얻을 수 있다.

# 특수문자
pyautogui.keyDown("shift")  # shift키를 누른 상태에서
pyautogui.write("4")  # 숫자 4를 입력하고
pyautogui.keyUp("shift")  # shift키를 땐다
pyautogui.write(["return"])

# 조합키 (Hot Key)
pyautogui.keyDown("Ctrl")
pyautogui.keyDown("a")
pyautogui.keyUp("a")  # press("a")
pyautogui.keyUp("ctrl")  # ctrl + A

# 간편한 조합키
pyautogui.hotkey("ctrl", "alt", "shift", "a")
  # ctrl 누르고 > alt 누르고 > shift 누르고 > A 누르고 > A 떼고 > shift 떼고 > alt 떼고 > ctrl 떼고

import pyperclip
pyperclip.copy("로키키키키키키킼")  # 해당 글자를 클립보드에 저장
pyautogui.hotkey("ctrl", "v")

def my_write(text):
    pyperclip.copy(text)  # 해당 글자를 클립보드에 저장
    pyautogui.hotkey("ctrl", "v")

my_write("캬캬캬컄컄ㅋ컄")


# 자동화 프로그램 종료
# win : ctrl + alt + del 
# mac : cmd + shift + option + q
