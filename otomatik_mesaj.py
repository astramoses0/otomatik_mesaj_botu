#Python Otomatik Mesaj Botu

import pyautogui
import time

time.sleep(1)

f=open("E:/instagram/a.txt","r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")

        
