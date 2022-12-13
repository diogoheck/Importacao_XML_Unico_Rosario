import pyautogui
from time import sleep


def acesso_inicial_NFSe(cliente, DT_inicial, DT_final, path, acesso_inicial):

    sleep(3)
    pyautogui.write(cliente)
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.write(DT_inicial)
    sleep(2)
    pyautogui.write(DT_final)
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(4)
    # if acesso_inicial:
    pyautogui.click(x=525, y=444, duration=2)
    # pyautogui.hotkey('backspace')
    sleep(2)
    # acesso_inicial = False
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
    # pyautogui.press('enter')
    sleep(2)
    print(path)
    pyautogui.write(path)
    sleep(2)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.press('enter')
