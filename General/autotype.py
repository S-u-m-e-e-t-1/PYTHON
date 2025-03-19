import pyautogui
import time
time.sleep(10)
count =0
while count!=10:
    pyautogui.typewrite("HAPPY NEW YEAR 2024 ")
    pyautogui.press("enter")
    count=count+1
