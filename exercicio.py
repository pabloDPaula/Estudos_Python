# COMANDO PARA COMENTAR E DESCOMENTAR - CTRL + /


# Exercicio 003 Somando dois números
# n1 = int(input('Digite um valor: '))
# n2 = int(input('Digite outro valor: '))
# print(f'A soma de {n1} com {n2} é {n1+n2}')


# Exercicio 004 Dissecando uma Variável
# a = input('Digite algo: ')
# print(f'O tipo da variável {a} é {type(a)}')


# Exercicio 006 Dobro, Triplo, Raiz Quadrada
# from math import sqrt as r
# a = int(input('Digite um valor: '))
# print(f'O dobro de {a} é {a*2}')
# print(f'O triplo de {a} é {a*3}')
# print(f'A raiz quadrada de {a} é {r(a):.2f}')


#Exercício Python #007 Média Aritmética
# n1 = int(input('Primeira nota do aluno: '))
# n2 = int(input('Segunda nota do aluno: '))
# print(f'A media entre {n1} e {n2} é igual a {(n1 + n2) / 2}')


#Exercício Python #008 Conversor de Medidas
# medida = float(input('Digite uma distância em metros: '))
# print(f'A medida de {medida}m corresponte a {medida * 100}cm e {medida * 1000}mm')


#Exercício Python #009 Tabuada
# numero = int(input('Digite um numero: '))
# for i in range(1,11):
#     print(f'{numero} x {i} é {numero * i}')

# Exercício Python #010 Conversor de Moedas
# moeda = float(input('Quanto voce tem na carteira? R$'))
# valor = moeda / 5.68
# print(f'Com R${moeda} você pode comprar US${valor:.2f}')


#Exercício Python #011 Pintando Parede
# larg = float(input('Largura da parede: '))
# alt = float(input('Altura da parede: '))
# area = larg * alt
# print(f'Sua prede tem a dimensão de {larg}x{alt} e sua área é de {area}m²')
# tinta = area / 2
# print(f'Para pintar essa parede, você precisará de {tinta}l de tints ')


#Exercício Python #012 Calculando desconto
# preco = float(input('Qual o preço do produto? R$ '))
# novo = preco - (preco * 0.05)
# print(f'O produto que custava R$ {preco}, na promção com desconto de 5% vai custar {novo:.2f}')


#Exercício Python #013 Reajuste Salarial
# salario = float(input('Qual é o salário do funcionário? R$ '))
# salarioNovo = salario + (salario * 0.15)
# print(f'Um funcionário que ganhava R$ {salario}, com 15% de aumento, passa a receber R$ {salarioNovo:.2f}')


#Exercício Python #014 Conversor de Temperaturas
# c = float(input('Informe a temperatura em ºC: '))
# f = 9 * c / 5 + 32
# print(f'A temperatura em {c}ºC corresponde a {f}ºF')


#Exercício Python #015 Aluguel de Carros
# dias = int(input('Quantos dias alugados? '))
# km = int(input('Quantos Km rodados?  '))
# total = (dias * 60) + (km * 0.15)
# print(f'O total a pagar é R$ {total:.2f}')


#Exercício Python #016 Quebrando um número
# import math
# numero = float(input('Digite um numero: '))
# print(f'O valor digitado foi {numero} e sua porção inteira é {math.trunc(numero)}')


#Exercício Python #019 Sorteando um item na lista
# import random
# nome1 = str(input('Primeiro aluno: '))
# nome2 = str(input('Segundo aluno: '))
# nome3 = str(input('Terceiro aluno: '))
# nome4 = str(input('Quarto aluno: '))
# escolhido = random.choice([nome1,nome2,nome3,nome4])
# print(f'O aluno escolhido foi {escolhido}')


#Exercício Python #020 Sorteando uma ordem na lista
# import random
# nome1 = str(input('Primeiro aluno: '))
# nome2 = str(input('Segundo aluno: '))
# nome3 = str(input('Terceiro aluno: '))
# nome4 = str(input('Quarto aluno: '))
# lista = [nome1,nome2,nome3,nome4]
# random.shuffle(lista)
# print(f'A ordem da lista será: ')
# print(lista)


#Exercício Python #022 Analisador de Textos
# nome = str(input('Digite seu nome completo: ')).strip()   - Tira os espaços do começo e do fim da palavra ou frase
# nomeCortado = nome.split()                                - Divide o nome completo em partes dentro de uma lista
# print('Analisando seu nome...')
# print(f'Seu nome em maiúsculo é {nome.upper()}')
# print(f'Seu nome em minúsculo é {nome.lower()}')
# print(f'Seu nome tem aotodo {len(nome) - nome.count(" ")} letras')
# print(f'Seu primeiro nome é {nomeCortado[0]} e ele tem {len(nomeCortado[0])} letras')


#Exercício Python #023 - Separando dígitos de um número
# num = input('Digite um número de até 4 dígitos: ')
# dic = {0: 'Milhar', 1: 'Centena', 2: 'Dezena', 3: 'Unidade'}
# for i,caracter in enumerate(num):
#     print(f'{dic[i]} {caracter}')


#Exercício Python #024 Verificando as primeiras letras de um texto
# cidade = (str(input('Em que cidade você nasceu? ')).strip()).upper()
# cidadeCortada = cidade.split()
# print(f'{"SANTO" in cidadeCortada}')


#Exercício Python #025 Procurando uma string dentro de outra
# nome = (str(input('Digite seu nome: ')).strip()).upper()
# nomeCortado = nome.split()
# print(f'{"SILVA" in nomeCortado}')


#Exercício Python #026 Primeira e última ocorrência de uma string
# frase = (str(input('Digite uma frase: ')).strip()).upper()
# print(f'A letra A aparece {frase.count("A")} vezes na frase')
# print(f'A primeira letra A apareceu na posição {frase.find("A") +1 }')
# print(f'A última letra A apareceu na posição {frase.rfind("A") + 1}')


#Exercício Python #027 Primeiro e último nome de uma pessoa
# nomeCompleto = str(input('Digite seu nome completo: ')).strip()
# nomeCortado = nomeCompleto.split()
# print(f'Seu primeiro nome é {nomeCortado[0]}')
# print(f'Seu último nome é {nomeCortado[ len(nomeCortado) - 1]}')


#Exercício Python #028 Jogo da Adivinhação v.1.0
# from random import randint
# from time import sleep
# numAleatorio = randint(0, 5)
# print('=====' * 11)
# print('Vou pensar em um numero entre 0 e 5. Tente Adivinhar')
# print('=====' * 11)
# num = int(input('Em que numero eu pensei? '))
# print('PROCESSANDO...')
# sleep(2)
# if num != numAleatorio:
#     print(f'Ganhei, Eu pensei no numero {numAleatorio} e não no {num}')
# else:
#     print('Parabéns, você ganhou')


#Exercício Python #029 Radar eletrônico
# velocidadeAtual = float(input('Qual é a velocidade do carro? Km '))
# if velocidadeAtual > 80:
#     multa = (velocidadeAtual - 80) * 7
#     print(f'''MULTADO!! Você excedeu o limite de velocidade de 80 Km/h
# Você deve pagar uma multa de R$ {multa:.2f}! ''')
# print('Tenha um bom dia e dirija com segurança')


#Exercício Python #030 - Par ou Ímpar?
# num = int(input('Digite um numero inteiro: '))
# if (num % 2) == 0:
#     print('Par')
# else:
#     print('Impar')


#Exercício Python #031 Custo da Viagem
# km = float(input('Qual é a distância da sua viagem? '))
# if km <= 200:
#     print(f'Você está prestes a começar uma viagem de {km:.0f} Km e que irá lhe custar {km * 0.50:.2f}')
# else:
#     print(f'Você está prestes a começar uma viagem de {km:.0f} Km e que irá lhe custar R$ {km * 0.45:.2f}')


#Exercício Python #033 Maior e menor valores
# num1 = int(input('Primeiro valor: '))
# num2 = int(input('Segundo valor: '))
# num3 = int(input('Terceiro valor: '))
# max = max([num1, num2, num3])
# min = min([num1, num2, num3])
# print(f'O maior valor digitado é {max}')
# print(f'O menor valor digitado é {min}')


#Exercício Python #034 Aumentos múltiplos
# salario = float(input('Qual é o salário do funcionário? R$'))
# if salario > 1250:
#     salarioNovo = salario + (salario * 0.10)
# else:
#     salarioNovo = salario + (salario * 0.15)
# print(f'O funcionário ganhava R$ {salario:.2f} e agora passa a ganhar R$ {salarioNovo:.2f}')


#Exercício Python #035 Analisando Triângulo v2.0
# s1 = float(input('Primeiro segmento: '))
# s2 = float(input('Segundo segmento: '))
# s3 = float(input('Terceiro segmento: '))
# if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
#     print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
#     if s1 == s2  == s3:
#         print('Equilátero')
#     elif s1 != s2 != s3 != s1:
#         print('Escaleno')
#     else :
#         print('Isósceles')
# else:
#     print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
#

#Exercício Python #036 Aprovando Empréstimo
# casa = float(input('Qual o valor da casa? R$ '))
# salario = float(input('Salário do comprador: R$ '))
# anos = int(input('Quantos anos de financiamento?'))
# prestacao = casa / (anos * 12)
# print(f'Para pagar uma casa de R$ {casa:.2f} em {anos} a prestação será de {prestacao:.2f}')
# if prestacao <= salario * 0.30:
#     print('Financiamento Aceito')
# else:
#     print('Financiamento Negado')


#Exercício Python #037 Conversor de Bases Numéricas
# numero = int(input('Digite um numero inteiro: '))
# print('''Escolha uma das bases para conversão
# [ 1 ] converter para BINÁRIO
# [ 2 ] converter para OCTAL
# [ 3 ] converter para HEXADECIMAL''')
# opcao = int(input('Digite sua opção: '))
# if opcao == 1:
#     print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)}')
# elif opcao == 2:
#     print(f'{numero} convertido para OCTAL é igual a {oct(numero)}')
# elif opcao == 3:
#     print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)}')
# else:
#     print('Opção inválida')


#Exercício Python #038 Comparando números
# num1 = int(input('Primeiro número: '))
# num2 = int(input('Segundo número: '))
# if num1 > num2:
#     print(f'PRIMEIRO número é maior')
# elif num2 > num1:
#     print(f'SEGUNDO número é maior')
# else:
#     print('Números iguais')


#Exercício Python #039  Alistamento Militar
# from datetime import date
# anoNascimento = int(input('Ano de nascimento: '))
# anoAtual = date.today().year
# idade = anoAtual - anoNascimento
# print(f'quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}')
# if idade == 18:
#     print('Já está na hora de se alistar')
# elif idade < 18:
#     saldo = 18 - idade
#     print(f'Você ainda tem {saldo} anos para se alistar \nseu alistamento será em {anoAtual + saldo} ')
# else:
#     saldo = idade - 18
#     print(f'Você deveria ter se alistado a {saldo} anos atrás, no ano de {anoAtual - saldo}')


#Exercício Python #040 Aquele clássico da Média
# nota1 = float(input('Primeira nota: '))
# nota2 = float(input('Segunda nota: '))
# media = (nota1 + nota2) / 2
# print(f'Tirando a média das notas {nota1} e {nota2} é {media}')
# if media < 5:
#     print('O aluno está REPROVADO')
# elif media >= 5 and media < 7:
#     print('O aluno está em recuperação')
# elif media >= 7:
#     print('O aluno está APROVADO')


#Exercício Python #041 Classificando Atletas
# from datetime import date
# anoNascimento = int(input('Ano de nascimento: '))
# idade = date.today().year - anoNascimento
# print(f'O atleta tem {idade} anos')
# if idade <= 9:
#     print('Categoria MIRIM')
# elif idade <= 14:
#     print('Categoria INFANTIL')
# elif idade <= 19:
#     print('Categoria JUNIOR')
# elif idade <= 25:
#     print('Categoria SÊNIOR')
# else:
#     print('Categoria MASTER')


#Exercício Python #043 Índice de Massa Corporal
# from math import pow
# peso = float(input('Qual é o seu peso? Kg '))
# altura = float(input('Qual é a sua altura? M '))
# imc = peso / pow(altura,2)       # imc = peso / altura * altura
# print(f'O IMC dessa pessoa é {imc:.1f}')
# if imc < 18.5:
#     print('Você está ABAIXO DO PESO')
# elif imc < 25:
#     print('Você está no PESO IDEAL')
# elif imc < 30:
#     print('Você está no SOBRE PESO')
# elif imc < 40:
#     print('Você tem OBESIDADE')
# else:
#     print('Você tem OBESIDADE MÓRBIDA')


#Exercício Python #044 Gerenciador de Pagamentos
# preco = float(input('Preço das compras: R$ '))
# print('''FORMAS DE PAGAMENTO
# [ 1 ] à vista dinheiro/cheque
# [ 2 ] à vista cartão
# [ 3 ] 2x no cartão
# [ 4 ] 3x ou mais no cartão''')
# opcao = int(input('Qual é a sua opção? '))
# if opcao == 1:
#     final = preco - ( preco * 0.1 )
#     print(f'Sua compra de R$ {preco:.2f} vai custar R$ {final:.2f} no final')
# elif opcao == 2:
#     final = preco - ( preco * 0.05 )
#     print(f'Sua compra de R$ {preco:.2f} vai custar R$ {final:.2f} no final')
# elif opcao == 3:
#     print(f'Sua compra vai custar R$ {preco / 2:.2f} no cartão, parcelado em 2x')
# elif opcao == 4:
#     totalparcelas = int(input('Quantas parcelas? '))
#     final = preco + preco * 0.2
#     print(f'Sua compra será parcelada em {totalparcelas}x de R$ {final/ totalparcelas:.2f} no cartão COM JUROS')
#     print(f'Sua compra de R$ {preco:.1f} vai custar R$ {final:.2f} no final')
# else:
#     print('Escolha inválida. Por favor, escolha uma das opções disponíveis')


#Exercício Python #045 GAME: Pedra Papel e Tesoura
# from random import randint
# from time import sleep
# regras = {0: 'Pedra',1: 'Papel',2:'Tesoura'}
# print('''Suas Opções:
# [ 0 ] PEDRA
# [ 1 ] PAPEL
# [ 2 ] TESOURA''')
# jogador = int(input('Qual é a sua jogada? '))
# computador  = randint(0,2)
# if jogador == 0 or jogador == 1 or jogador == 2:
#     print('JO')
#     sleep(1)
#     print('KEN')
#     sleep(1)
#     print('PO')
#     sleep(1)
#     if jogador == computador:
#         print('EMPATE !!')
#     elif ( jogador == 0 and computador == 2 ) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
#         print('JOGADOR VENCE')
#     elif ( jogador == 0 and computador ==  1) or (jogador == 1 and computador == 2) or (jogador == 2 and computador == 0):
#         print('JOGADOR PERDE')
#     print('-=-'*10)
#     print(f'Jogador escolheu {regras[jogador]}')
#     print(f'Computador escolheu {regras[computador]}')
#     print('-=-'*10)
# else:
#     print('Opção inválida')
