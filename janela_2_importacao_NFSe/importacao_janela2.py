from smtpd import PureProxy
import pyautogui
import time
import os


def importar_notas_final(cliente):
    box = None
    pyautogui.click()
    while(pyautogui.locateOnScreen('botao_importar.png') == None):
        pass
        # print('aguardando botao importar')
    time.sleep(2)
    pyautogui.click(pyautogui.click(x=97, y=119), duration=0.5)
    time.sleep(40)
    box = pyautogui.locateOnScreen('informacao.png')
    time.sleep(2)
    print(box, cliente)
    if box:
        pyautogui.click(x=874, y=496)
        time.sleep(2)
        pyautogui.click(x=987, y=587)
        time.sleep(2)
        pyautogui.click(x=1342, y=98)
        time.sleep(2)
        pyautogui.press('enter')
        time.sleep(2)
        # os.rename(f'u:\\ISS\\xml\\{cliente}', f'u:\\ISS\\xml\\{cliente}OK')
    else:
        time.sleep(2)
        pyautogui.click(x=773, y=437)
        time.sleep(2)
