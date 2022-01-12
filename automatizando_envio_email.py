import pyautogui
import pyperclip   # copiar texto ou frases por causa dos caracteres especiais: ?, $, %,&
from time import sleep
import pandas as pd

pyautogui.PAUSE = 1   # pausa o codigo de cada linha em 1s para não fazer tudo direto
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")
pyperclip.copy("https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
sleep(2)
pyautogui.doubleClick(x=403, y=292)
sleep(2)
pyautogui.click(x=416, y=348)
pyautogui.click(x=1655, y=182)
pyautogui.click(x=1498, y=589)
#pega a posição do mouse
# sleep(5) para dar tempo de posicionar o mouse
#print(pyautogui.position())
sleep(2)
tabela = pd.read_excel("C:\\Users\\pablo\\Downloads\\Vendas - Dez.xlsx")
#print(tabela)
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()
pyautogui.hotkey("ctrl","t")
pyperclip.copy("mail.google.com/mail/u/0/?tab=wm#inbox")
pyautogui.hotkey("ctrl","v")
pyautogui.press("enter")
sleep(3)
pyautogui.click(x=72, y=209)
sleep(1)
pyautogui.write("pablopaulo2009@gmail.com")
pyautogui.hotkey("tab")
pyautogui.hotkey("tab")
assunto = "Relatório de vendas de ontem"
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")
texto = f"""Prezados, bom dia

O faturamento de ontem foi de : R$ {faturamento:.2f}
A quantida de produtos foi de {quantidade:.2f}

abs
Pablo
"""
pyperclip.copy(texto)
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("ctrl","enter")


