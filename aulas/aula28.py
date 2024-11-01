nome = str(input('Digite seu nome: '))
idade = str(input('Digite sua idade: ')).strip()
if nome.strip() == '' or idade.strip() == '':
    print('Desculpe, vece deixou campos vazio.')
else:
    print(f'Seu nome e {nome}')
    print(f'Sou nome invertido e {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome tem espacos.')
    else:
        print('Seu nome nao tem espacos.')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome e {nome[0]}')
    print(f'A ultima letra do seu nome e {nome[-1]}')
    