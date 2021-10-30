#Python Otomatik Mesaj Botu
import pyautogui
import time

time.sleep(1)

while True:
    f= open(".txt path here","r")


    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")