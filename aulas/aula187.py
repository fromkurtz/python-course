# sys.argv - Executando arquivos com argumentos no sistema
import sys

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Voce nao passou argumentos')
else:
    try:
        print(f'Voce passou os argumentos {argumentos[1:]}')
        print(f'faca alguma coisa com o {argumentos[1]}')
        print(f'faca outra coisa com o {argumentos[2]}')
    except IndexError:
        print('faltam argumentos')
