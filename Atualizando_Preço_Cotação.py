# Será usado Selenium
# Selenium é uma biblioteca que permite com que o Python abra o seu navegador para executar os comandos desejados.( automatização somente do navegador)
# Webdriver do chrome -> chromedriver ( coloque na pasta do python )

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
pd.set_option('max_columns', 10)

navegador = webdriver.Chrome()

#Documentação do Selenium - https://selenium-python.readthedocs.io/locating-elements.html
#   Passo 1: pegar a cotação do Dolar - 5.53

navegador.get("https://www.google.com.br") # -> selenium espera o navegador carregar, diferente do pyautogui
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys("Cotação dolar")
#Caminho ( Path ) do campo de busca:  Ctrl + Shift + C e aperte no elemento e cole o html do elemento acima depois do By.XPATH

# navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click() OU
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys(Keys.ENTER)

cotacao_dolar = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")


#   Passo 2: pegar a cotação do Euro  - 6.33

navegador.get("https://www.google.com.br") # -> abre o google
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys("Cotação Euro") # Pesquisa "Cotação Euro no Pesquisar"
navegador.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div[2]/div[2]/input').send_keys(Keys.ENTER) # Aperta o ENTER
cotacao_euro = navegador.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value") # Pega o valor guardado no data-value

#   Passo 3: pegar a cotação do Ouro -  325,93
navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_ouro = navegador.find_element(By.XPATH,'//*[@id="comercial"]').get_attribute("value")
cotacao_ouro = cotacao_ouro.replace(",",".") # Replace troca a "," pelo "."


#   Passo 4: Importar base de dados e atualizar as cotações na minha base
tabela = pd.read_excel("Produtos.xlsx")
print(tabela)
print("-=-"*20)
print("\n")

tabela.loc[tabela['Moeda'] == "Dólar", 'Cotação'] = float(cotacao_dolar)
# TODAS as linhas onde a moeda for dolar, ele altera a cotação para esse novo valor em float
tabela.loc[tabela['Moeda'] == "Euro", 'Cotação'] = float(cotacao_euro)
tabela.loc[tabela['Moeda'] == "Ouro", 'Cotação'] = float(cotacao_ouro)

#   Passo 4: Calcular novos preços e salvar/exportar a base de dados

# Preço de Compra = Preço original * Cotação
tabela['Preço de Compra'] = tabela['Preço Original'] * tabela['Cotação']

# Preço de venda = Preço de venda * Margem
tabela['Preço de Venda'] = tabela['Preço de Venda'] * tabela['Margem']

print(tabela)

tabela.to_excel("Produtos novos.xlsx",index=False)