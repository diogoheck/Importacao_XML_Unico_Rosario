import pyautogui
import time

# time.sleep(10)
# print(pyautogui.position())

while(pyautogui.locateOnScreen('botao_importar.png') == None):
    print('none')
