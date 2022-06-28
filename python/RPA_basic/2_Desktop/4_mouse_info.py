import pyautogui

# pyautogui.mouseInfo() # 마우스 정보 표시
pyautogui.PAUSE = 1  # 모든 동작에 1초씩 sleep 적용

# pyautogui.FAILSAFE = False  # 마우스 가생이에 가져다놓으면 취소안되게
# raise FailSafeException(
# pyautogui.FailSafeException: PyAutoGUI fail-safe triggered from mouse moving to a corner of the screen. To disable this fail-safe, set pyautogui.FAILSAFE to False. DISABLING FAIL-SAFE IS NOT RECOMMENDED.
for i in range(10):
    pyautogui.move(100, 100)
    pyautogui.sleep(1)
