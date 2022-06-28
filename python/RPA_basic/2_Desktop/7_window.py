# 맥os는 지원을 하지 않습니다.
import pyautogui

# fw = pyautogui.getActiveWindow()  # 현재 활성화 된 창
# print(fw.title)  # 창의 제목 정보
# print(fw.size)  # 창의 크기 정보(width, height)
# print(fw.left, fw.right, fw.top, fw.bottom)  # 창의 좌표 정보
# pyautogui.click(fw.left + 100, fw.top + 100)  # 창이 이동해도 창으 기준으로 실행이 됩니다.
#
# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle("new 1 - Notepad++")[0]
print(w)

if w.isActive == False:  # 현재 활성화가 안 되어있으면
    w.activate()  # 활성화

if w.isMaximized == False:
    w.maximize()

pyautogui.sleep(1)

if w.isMinimized == False:
    w.minimize()

w.restore()
w.close()
