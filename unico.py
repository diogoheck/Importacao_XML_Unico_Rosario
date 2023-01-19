from Login.login_unico import logar_unico
from modulo_fiscal.selecionar_mod_fiscal import acessar_modulo_fiscal
from modulo_import_municipal.importacao_municipal import acessar_modulo_importacao_municipal
from janela_1_importacao_NFSe.primeiro_acesso import acesso_inicial_NFSe
from janela_2_importacao_NFSe.importacao_janela2 import importar_notas_final

import pyautogui
import os
DT_inicial = '01122022'
DT_final = '31122022'

LOCAL_GRAVAR_LOGS = 'R:\Compartilhado\Ti\log_NFSe_jose\log_jose.txt'

def salvar_logs(conteudo):
    with open(LOCAL_GRAVAR_LOGS, 'a', encoding='ansi') as log:
        print(conteudo, file=log)


if __name__ == '__main__':

    # logar_unico()
    acessar_modulo_fiscal()
    acessar_modulo_importacao_municipal()
    acesso_inicial = True
    lista_pastas = os.listdir(f'U:\\Tributario\\Jose Abdes\\NFS\\2022')
    
   
    for path in os.listdir(f'U:\\Tributario\\Jose Abdes\\NFS\\2022'):
       
        full_path = f'X:\\Tributario\\Jose Abdes\\NFS\\2022' + os.sep + path
        
        acesso_inicial_NFSe('2149', DT_inicial, DT_final,
                            full_path, acesso_inicial)
        importar_notas_final('2149')
        salvar_logs(path)
        
        


    pyautogui.click(x=979, y=309)
    pyautogui.click(x=1338, y=2)
    pyautogui.click(x=653, y=439)
    pyautogui.press('enter')

    print('*' * 50)
    print('*' * 50)
    print('finalizado com sucesso')
    print('*' * 50)
    print('*' * 50)