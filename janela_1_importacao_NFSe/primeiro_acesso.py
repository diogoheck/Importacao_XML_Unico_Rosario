import pyautogui
from time import sleep


def acesso_inicial_NFSe(cliente, DT_inicial, DT_final, path, acesso_inicial):

    sleep(3)
    pyautogui.write(cliente)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.write(DT_inicial)
    sleep(1)
    pyautogui.write(DT_final)
    sleep(1)
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    sleep(1)
    # if acesso_inicial:
    pyautogui.click(x=525, y=444, duration=1)
    # pyautogui.hotkey('backspace')
    sleep(1)
    # acesso_inicial = False
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('enter')
    # pyautogui.press('enter')
    sleep(1)
    print(path)
    pyautogui.write(path)
    pyautogui.press('enter')
    pyautogui.press('enter')
