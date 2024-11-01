import os

palavra_secreta = 'computador'
letras_acertadas = ''
numero_tentativas = 0

while True:
    resp = input('Digite uma letra: ').strip().lower()
    numero_tentativas += 1

    if len(resp) > 1:
        print('Digite apenas uma letra! ')
        continue

    if resp in palavra_secreta:
        letras_acertadas += resp

    palavra_formada= ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('VOCE GANHOU!!')
        print(f'A palavra era {palavra_secreta}')
        print(f'tentativas: {numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0

    

    
