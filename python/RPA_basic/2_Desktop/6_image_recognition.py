import pyautogui

file_menu = pyautogui.locateOnScreen("file_menu.png")
print(file_menu)
pyautogui.click(file_menu)

# x_icon = pyautogui.locateOnScreen("X_icon.png")
# pyautogui.moveTo(x_icon)

# screen = pyautogui.locateOnScreen("screenshot.png")
# print(screen)

# for i in pyautogui.locateAllOnScreen("checkbox.png"):   # 여려개의 이미지를 조정하고 싶을 때
#     print(i)
#     pyautogui.click(i, duration=0.25)

# checkbox = pyautogui.locateOnScreen("checkbox.png")  # 제일 처음 만난 이미지에 해당하는 그림을 실행
# pyautogui.click(checkbox)

# 속도 개선
# 1. GrayScale : 흑백모드
# checkbox = pyautogui.locateOnScreen("checkbox.png", grayscale=True)
# pyautogui.click(checkbox)

# 2. 범위를 지정
# checkbox = pyautogui.locateOnScreen("checkbox.png", region = (x, y, width, height)
# pyautogui.click(checkbox)

# 3. 정확도 조정
# pip install opencv-python
# run_btn = pyautogui.locateOnScreen("run.png", confidence=0.9)
# pyautogui.moveTo(run_btn)

# 자동화 대상 이미지가 바로 보여지지 않는 경우
file_notepad = pyautogui.locateOnScreen("file_notepad.png")

# # 1. 계속 기다리기
# if file_notepad:
#     pyautogui.click(file_notepad)
# else:
#     print("cannot find location")

# while file_notepad is None:
#     file_notepad = pyautogui.locateOnScreen("file_notepad.png")
#     print("cannot find location")
# pyautogui.click(file_notepad)

# 2. 일정시간 기다리기
import time
import sys


# timeout = 5  # 대기시간
# start_time = time.time()  # 시작시간 설정
# file_notepad = None
# while file_notepad is None:
#     file_notepad = pyautogui.locateOnScreen("file_notepad.png")
#     end_time = time.time()  # 종료시간 설정
#     if end_time - start_time > timeout:  # 지정한 시간을 초과하면 종료
#         print("time over")
#         sys.exit()
#
# pyautogui.click(file_notepad)

def find_target(img_file, timeout=10):
    start_time = time.time()  # 시작시간 설정
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end_time = time.time()  # 종료시간 설정
        if end_time - start_time > timeout:  # 지정한 시간을 초과하면 종료
            break
    return target


def my_click(img_file, timeout=10):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
        print("Target found")
    else:
        print("[Time out {}s] Target not found \"{}\". Terminate program.".format(timeout, img_file))
        sys.exit()


my_click("file_notepad.png", 5)

