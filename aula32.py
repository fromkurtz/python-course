# Exercicio 1: 
""" 
try:
    numero = int(input('Digite um numero inteiro: '))
    if numero % 2 == 0:
        print('O numero digitado e PAR.')
    else:
        print('O numero digitado e IMPAR.')
except:
    print('O numero digitado nao e Inteiro!')

"""

#Exercicio 2:
"""
hora = int(input('Qual a hora no nomemento? '))
if 0 < hora <= 11:
    print('Bom dia!')
elif 12 <= hora <= 17:
    print('Boa tarde!')
elif hora > 24:
    print('Hora invalida!')
else:
    print('Boa noite!')

"""

#Exercicio 3:

nome = str(input('Digite seu primeiro nome: '))
quantidade_letras = len(nome)
if quantidade_letras <= 4:
    print('Seu nome e curto!')
elif 4 < quantidade_letras <=6:
    print('Seu nome e de tamanho normal!')
else:
    print('Seu nome e muito grande! ')
    