#Taller 1 
def genCiclosHamiltoneanos(G,nodo,lista,nodos,nodoInicial):  
    cont = 0
    for i in G[nodo]:
        if len(lista) < (len(G)-1) or nodo == nodoInicial:
            if i:
                if cont not in lista and cont != nodos:
                    if cont not in lista:
                        if nodo not in lista:
                            lista.append(nodo)
                        nodos = -1
                        yield from genCiclosHamiltoneanos(G,cont,lista,nodos,nodoInicial)
                else:
                    cont +=1
            else:
                cont +=1       
    if len(lista) != len(G):
        nodoFinal = nodo
        posicionFinal = G[nodoFinal]
        posicionInicial =G[nodoInicial]
        if posicionFinal[nodoInicial] == True and posicionInicial[nodoFinal] == True and len(lista) == (len(G)-1):
            lista.append(nodo)
            yield lista
        else:
            nodos = lista.pop()
            yield from genCiclosHamiltoneanos(G,lista[len(lista)-1],lista,nodos,nodoInicial)
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