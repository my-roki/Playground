# Quiz) 아래 동작을 자동으로 수행하는 프로그램을 작성하시오.
# 1. 그림판 실행 (단축키 : win + r, 입력값 : mspaint) 및 최대화
# 2. 상단의 텍스트 기능을 이용하여 흰 영역 아무 곳에다가 글자 입력
#     - 입력 글자 : "참 잘했어요~"
# 3. 5초 대기 후 그림판 종료
#     이 때, 저장하지 않음을 자동으로 선택하여 프로그램이 완전 종료되도록 함

import pyautogui
import pyperclip

def my_write(text):
    pyperclip.copy(text)  # 해당 글자를 클립보드에 저장
    pyautogui.hotkey("ctrl", "v")

# 시작~~ 하겠읍니다~~~
print("RPA is start soon...")
pyautogui.countdown(3)
print("RPA is running")

# 그림판 실행 및 최대화
pyautogui.hotkey("win", "r")
pyautogui.sleep(1)
pyautogui.write("mspaint", interval=0.25)
pyautogui.press("enter")

pyautogui.sleep(1)
paint = pyautogui.getWindowsWithTitle("제목 없음 - 그림판")[0]
if paint.isActive == False:  
    paint.activate()

pyautogui.sleep(1)

if paint.isMaximized == False:
    paint.maximize()


# 그림판 안에 텍스트 문구를 찾고 클릭
text_box_img = r"D:\workpractice\RPA_basic\2_Desktop\quiz_img\text_box.png"
text_box = pyautogui.locateOnScreen(text_box_img)
pyautogui.click(text_box, interval=0.25)

# 흰 화면으로 이동 후 문구 작성
pyautogui.move(0, 300, duration=1)
pyautogui.sleep(1)
pyautogui.click()
my_write("참 잘했어요")

# 5초 대기
pyautogui.sleep(5)

# 닫고 저장 안함
# window.close()
pyautogui.moveTo(1900, 10, duration=1)
pyautogui.click()

pyautogui.sleep(1)
pyautogui.press("n")

# not_save_img = r"D:\workpractice\RPA_basic\2_Desktop\quiz_img\not_save.png"
# not_save = pyautogui.locateOnScreen(not_save_img)
# pyautogui.click(not_save, interval=0.25)
 
