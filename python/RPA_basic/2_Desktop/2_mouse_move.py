import pyautogui

# 절대좌표로 마우스 이동
pyautogui.moveTo(200, 100)  # 지정한 위치(가로x, 세로y)로 마우스 이동
pyautogui.moveTo(500, 500, duration=2)  # duration(초) 동안 좌표로 이동

pyautogui.moveTo(100, 100, duration=2)
pyautogui.moveTo(200, 300, duration=2)
pyautogui.moveTo(300, 500, duration=2)

# 상대좌표로 마우스 이동
pyautogui.moveTo(100, 100, duration=1)
print(pyautogui.position())  # point(x, y)
pyautogui.move(100, 200, duration=1)  # 100, 100 기준으로 +100, +200 -> (200, 300)으로 이동
print(pyautogui.position())  # point(x, y)
pyautogui.move(100, 300, duration=1)  # 200, 200 기준으로 +100, +300 -> (300, 600)으로 이동
print(pyautogui.position())  # point(x, y)

p = pyautogui.position()
print(p[0], p[1])  # x, y
print(p.x, p.y)  # x, y
