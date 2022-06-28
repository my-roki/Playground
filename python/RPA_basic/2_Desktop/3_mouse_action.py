import pyautogui

pyautogui.sleep(3)  # 3초 대기
print(pyautogui.position())

pyautogui.click(1975, 20, duration=1)  # 1초동안 해당 좌표로 이동 후 마우스 클릭
pyautogui.click()  # 클릭
pyautogui.mouseDown()  # 마우스 버튼 누른 상태
pyautogui.mouseUp()  # 마우스 버튼 뗀 상태
pyautogui.doubleClick()  # 더블클릭

pyautogui.sleep(3)
pyautogui.click(clicks=500)

pyautogui.sleep(3)
pyautogui.moveTo(300, 300)
pyautogui.mouseDown()
pyautogui.moveTo(500, 500)
pyautogui.mouseUp() 

pyautogui.sleep(3)
pyautogui.rightClick()  # 오른쪽 클릭
pyautogui.middleClick()  # 휠 클릭

pyautogui.sleep(3)
print(pyautogui.position())
pyautogui.moveTo(3081, 345)
pyautogui.drag(200, 200, duration=0.25)  # 현재위치를 기준으로 해당 좌표만큼 드래그
pyautogui.dragTo(3018, 345, duration=0.25)  # 절대좌표 기준으로 x, y 좌표로 이동

pyautogui.scroll(500)  # 양수이면 위 방향으로 스크롤
pyautogui.scroll(-500)  # 음수이면 아래 방향으로 스크롤
