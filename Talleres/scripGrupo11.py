#Taller 1 
def genCiclosHamiltoneanos(G,nodo,lista,nodos,nodoInicial):  
    cont = 0
    for i in G[nodo]:
        if len(lista) < (len(G)-1):
            if i:
                if cont not in lista and cont != nodos:
                    if cont not in lista:
                        if nodo not in lista:
                            lista.append(nodo)
                        nodos = -1
                        next(genCiclosHamiltoneanos(G,cont,lista,nodos,nodoInicial))
                else:
                    cont +=1
            else:
                cont +=1
        #else:
    if len(lista) != len(G):
        nodos = lista.pop()
        next(genCiclosHamiltoneanos(G,lista[len(lista)-1],lista,nodos,nodoInicial))
    else:
        yield lista


G = [
    [False,True,True,False,True],
    [True,False,True,True,False],
    [True,True,False,False,True],
    [False, True, False, False, True],
    [True,False, True, True, False]
]

listaAux = []
listaFinal = -1
print(next(genCiclosHamiltoneanos(G,0,listaAux,listaFinal,0)))