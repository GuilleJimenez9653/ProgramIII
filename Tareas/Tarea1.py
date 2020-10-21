def esPar(tupla):
    par = True
    for i in tupla:
        if par == True and i%2 != 0:
            par = False
    return par

tupla1 = (1,2,3,4,5,6,7,8,9)
tupla2 = (2,4,6,8,10)
tupla3 = (20,30,40,50)
tupla4 = (33,34,35,36)
lista = [tupla1,tupla2,tupla3,tupla4]
listafinal = []

for i in lista:
    if esPar(i):
        listafinal.append(i)
print(listafinal)