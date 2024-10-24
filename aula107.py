#def zipper(lista1, lista2):
#    menor_lista = min(len(lista1), len(lista2))
#    return [(lista1[i], lista2[i]) for i in range#(menor_lista)]


#cidades = ['Salvador', 'Ubatuba', 'Belo #horizonte']
#siglas = ['Ba', 'SP', 'MG', 'RJ']
#print(zipper(cidades, siglas))
cidades = ['Salvador', 'Ubatuba', 'Belo #horizonte']
siglas = ['Ba', 'SP', 'MG', 'RJ']
print(list(zip(cidades, siglas)))