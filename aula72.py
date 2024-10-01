def multiplicando(*x):
    total = 1
    for numeros in x:
        total *= numeros
    return total


def ParOuImpar(x):
    if x % 2 == 0:
        return f'O numero {x} e Par!'
    return f'O numero {x} e Impar!'


soma_total = multiplicando(1, 2, 3, 4, 5)
print(soma_total)

par_impar = ParOuImpar(7)
print(par_impar)
