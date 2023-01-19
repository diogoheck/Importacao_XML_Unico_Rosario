import pyautogui
from time import sleep


def acessar_modulo_importacao_municipal():
    sleep(2)
    pyautogui.hotkey('alt', 'i')
    sleep(2)
    pyautogui.click(x=724, y=409)
    sleep(5)

if __name__ == '__main__':
    acessar_modulo_importacao_municipal()
