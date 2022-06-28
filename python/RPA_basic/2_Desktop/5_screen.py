import pyautogui

# # 스크린샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")  # 파일로 저장

# pyautogui.mouseInfo()
# 99,130 255,0,0 #FF0000

pixel = pyautogui.pixel(99, 130)
print(pixel)


print(pyautogui.pixelMatchesColor(99, 130, (255, 0, 0)))
print(pyautogui.pixelMatchesColor(99, 130, pixel))
print(pyautogui.pixelMatchesColor(99, 130, (255, 255, 0)))

