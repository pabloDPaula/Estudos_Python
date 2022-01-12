import pandas as pd
import plotly.express as px

    # Passo 1: Importar base de dados
tabela = pd.read_csv("telecom_users.csv")

# opção no pandas para exibir toda a coluna no print e não só metade como padrão
pd.set_option('max_columns', 10)

    # Passo 2: Visualizar base de dados
print(tabela)
print("-=-"*20)
print("\n")

    # Passo 3: Tratamento de dados( corrigir problemas na base de dados)
# - Coluna inútil
# Axis = 0 -> Linha
# EXEMPLO: tabela = tabela.drop(3,axis = 0)
# Axis = 1 -> Coluna
tabela = tabela.drop("Unnamed: 0",axis=1)

# documentação da biblioteca pandas - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html
print(tabela.info())   # verbose true para mostrar a tabela toda
print("-=-"*20)
print("\n")
"""
non-null = não nulo , ou seja, está cheio 
Coluna Dependentes e Churn tem 1 valor vazio, ou seja, null. 
Porque todas as outras colunas tem 5986 valores não nulo enquanto que dependentes tem 5985 valores não nulos.

Coluna codigo está totalmente vazia, todos os valores são null ( NaN)

Coluna TotalGasto está sendo reconhecido como texto( object ) e não como numero ( float64 )
"""
# - Valores reconhecidos de forma errada

# documentação do to_nmeric - https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html
# errors="coerce" caso ele não consiga mudar o valor de texto para numero, ele coloca o valor como NaN ( vazio)
# Exemplo: não tem como mudar o tipo de "lira" para numero, só "56" para 56
tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"],errors="coerce")

# - Tratar valores vazios NaN
# documentação do dropna - https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html
# Exclui todas as linhas e colunas que tenham valor Nan ( vazio)
tabela = tabela.dropna(how="all",axis=1) # Exclui todas as colunas vazias, ou seja, todos os valores são NaN
tabela = tabela.dropna(how="any",axis=0) # Exclui as linhas que possuem algum valor vazio ( NaN ) presente nela
print(tabela.info())
print("-=-"*20)
print("\n")

    # Passo 4: Analise inicial
# conta todos os valores na tabela Churn ( cancelamento )
print(tabela["Churn"].value_counts())
# Exibi como porcentagem
print(tabela["Churn"].value_counts(normalize=True).map("{:.1%}".format))

    # Passo 5: Analise detalhada dos clientes
for coluna in tabela.columns:
    grafico = px.histogram(tabela,x=coluna,color="Churn")
    grafico.show()