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
    time.sleep(1)
    pyautogui.click(pyautogui.click(x=97, y=119), duration=0.5)
    time.sleep(15)
    box = pyautogui.locateOnScreen('informacao.png')
    print(box, cliente)
    if box:
        pyautogui.click(x=874, y=496)
        time.sleep(1)
        pyautogui.click(x=987, y=587)
        pyautogui.click(x=1342, y=98)
        pyautogui.press('enter')
        # os.rename(f'u:\\ISS\\xml\\{cliente}', f'u:\\ISS\\xml\\{cliente}OK')
    else:
        pyautogui.click(x=773, y=437)
