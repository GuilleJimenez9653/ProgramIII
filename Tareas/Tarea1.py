import random

def esPar(tupla):
    par = True
    for i in tupla:
        if par == True and i%2 != 0:
            par = False
    return par

def organizarTuplas(lista):
    listafinal = []
    for i in lista:
        if esPar(i):
            listafinal.append(i)
    return listafinal

lista = []
tupla = ()
for i in range(0,5):
    lista_aux = []
    for j in range(0,2):
        x = random.randint(0,10)
        lista_aux.append(x)
    tupla = lista_aux
    tupla = tuple(tupla)
    lista.append(tupla)

print(organizarTuplas(lista))