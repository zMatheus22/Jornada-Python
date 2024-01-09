# Passo a passo do projeto

# Projeto 1 - Entrar no sitema da empresa 
    # "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Importando o pyautogui
import pyautogui
from time import sleep

# click -> pyautogui.click
# escrever -> pyautogui.write
# apertar uma tecla -> pyautogui.press
# apertar -> pyautogui.hotkey

# A cada comando da um pause de 0.5s
pyautogui.PAUSE = 0.5

# Aperta a tecla do windows (command + barra de espaço)
pyautogui.press("win")

# Digitar o nome do programa (edge)
pyautogui.write("edge")

# Apertar enter
pyautogui.press("enter")

# Digitar o link 
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# Apertar enter
pyautogui.press("enter")

# Esperar 3 segundos
sleep(3)

#----------------------------#
# Passo 2 - Fazer login

pyautogui.click(x=876, y= 351)

# Digitar o email
pyautogui.write("email@gmail.com")

# Passa para a próximo campo
pyautogui.press("tab")

# Digitar a Senha
pyautogui.write("senha123")

# Passa para a próximo campo
pyautogui.press("tab")

# Dar enter no botão do login
pyautogui.press("enter")

# Esperar 3 segundos
sleep(3)

#----------------------------#
# Passo 3 - Importar a base de dados

# pip install pandas numpy openpyxl
import pandas

# Ler o arquivo
tabela = pandas.read_csv("produtos.csv")

#----------------------------#
# Passo 4 - Cadastra um produto


# Percore cada linha da tabela
for linha in tabela.index:

    # Click no código do produto
    pyautogui.click(x=903, y=237)
    
    # Digitar os campos e passar para o próximos campos.
    # Codigo
    pyautogui.write(tabela.loc[linha,"codigo"])
    # Marca
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha,"marca"])
    # Tipo
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[linha,"tipo"])
    # Categoria
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    # Preço Unitário
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    # Custo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha,"custo"]))
    # OBS
    pyautogui.press("tab")
    # Tratamento de erro (NaN)
    obs = tabela.loc[linha,"obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)
    # Botão "Enviar"
    pyautogui.press("tab")
    pyautogui.press("enter")
    # Dar scroll para o inicio
    pyautogui.scroll(5000)
