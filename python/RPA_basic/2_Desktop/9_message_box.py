import pyautogui

print("RPA is start soon...")
pyautogui.countdown(3)
print("RPA is running")

pyautogui.alert("Failed RPA", "Warning")  # 확인 버튼만 있는 팝업

result = pyautogui.confirm("Continue?", "Yes")  # 확인, 취소 버튼
print(result)

result = pyautogui.prompt("input text", "input")  # 사용자 입력
print(result)

result = pyautogui.password("input password")  # 암호 입력
print(result)

# https://pyautogui.readthedocs.io/en/latest/
# 위 사이트에서 pyautogui에 대한 더 많은 공부를 할 수 있습니다.
