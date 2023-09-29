import pyautogui
import time

def clicar(imagem, clique_dublo=False):
    while True:
        time.sleep(0.5)
        if pyautogui.locateCenterOnScreen(imagem, confidence=0.7):
            pesquisa = pyautogui.locateCenterOnScreen(imagem, confidence=0.7)
            pyautogui.click(pesquisa.x, pesquisa.y)
            if clique_dublo:
                pyautogui.click(pesquisa.x, pesquisa.y)
            break
        

def escreve_clicar(texto):
    pyautogui.write(texto)
    pyautogui.press('enter')


pyautogui.press('winleft')
pyautogui.write('chrome')
time.sleep(0.2)
pyautogui.press('enter')

clicar(r'assets\navegador-gabriel.png', clique_dublo=True)
clicar(r'assets\pesquisa-google.png')
escreve_clicar('https://gerais.defensoria.mg.def.br/sistemas/scsdp/')
clicar(r'assets\btn-interno.png')
clicar(r'assets\btn-acesso.png')
clicar(r'assets\menu-gerais.png')
time.sleep(1)
clicar(r'assets\grupo-sti.png')
clicar(r'assets\sgp.png')
clicar(r'assets\novo-produtividade.png')
clicar(r'assets\Prestacao-acao.png')
clicar(r'assets\outros.png')
clicar(r'assets\quantidade.png')
pyautogui.write('1')
clicar(r'assets\atividade.png')
clicar(r'assets\ordinaria.png')
clicar(r'assets\descricao.png')
pyautogui.write('Realizei atividades relacionadas a rotina de tratamento de dados no Banco de Dados da DPMG.')