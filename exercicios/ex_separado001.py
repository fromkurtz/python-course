def cabecalho():
    print('=='*20)
    print(f'{"OPCOES DE OPERACAOES": ^40}')
    print('=='*20)
    print(f'''{"""
        (1) Adicao
        (2) Subtracao
        (3) Multiplicao
        (4) Divisao
     """}''')
    print('=='*20)


n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
cabecalho()
r = int(input('Digite a opcao: '))
if r < 1 or r > 4:
    while True:
        print('Opcao invalida, digite novamente.')
        r = int(input('Digite Novamente: '))
        if 0 < r < 5:
            break

match r:
    case 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    case 2:
        print(f'{n1} - {n2} = {n1 - n2}')
    case 3:
        print(f'{n1} x {n2} = {n1 * n2}')
    case 4:
        print(f'{n1} / {n2} = {n1 / n2}')
