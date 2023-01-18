import pyautogui

screenWidth, screenHeight = pyautogui.size()
print("Ekran Çözünürlüğü :", screenWidth, screenHeight)


currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)