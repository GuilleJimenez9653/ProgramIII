#Taller 1 
def genCiclosHamiltoneanos1(G,nodo,lista,nodos,nodoInicial,listaAux):  
    cont = 0
    for i in G[nodo]:
        if len(lista) < (len(G)-1) or nodo == nodoInicial:
            if i:
                if cont not in lista and cont != nodos:
                    if cont not in lista:
                        if nodo not in lista:
                            lista.append(nodo)
                        nodos = -1
                        yield from genCiclosHamiltoneanos1(G,cont,lista,nodos,nodoInicial,listaAux)
                else:
                    cont +=1
            else:
                cont +=1       
    if len(lista) != len(G):
        posicionFinal = G[nodo]
        posicionInicial =G[nodoInicial]
        if posicionFinal[nodoInicial] == True and posicionInicial[nodo] == True and len(lista) == (len(G)-1):
            lista.append(nodo)
            yield lista
        else:
            nodos = lista.pop()
            yield from genCiclosHamiltoneanos1(G,lista[len(lista)-1],lista,nodos,nodoInicial,listaAux)
    else:
        yield lista

def genCiclosHamiltoneanos(G,nodo,camino,nodoInicial):
    cont = 0
    for i in G[nodo]:
        if esHamiltoneano(G,camino,cont,nodoInicial) and cont not in camino and cont < len(G):
            yield camino + [cont]
        cont += 1
    cont = 0
    for i in G[nodo]:
        if G[nodo] and cont not in camino and i and cont < len(G) and esAdyacente(G,camino[len(camino)-1],cont):
            yield from genCiclosHamiltoneanos(G,cont,camino + [cont],nodoInicial)
        cont += 1

def esHamiltoneano(G,camino,nodo,nodoInicial):
    posicionFinal = G[nodo]
    posicionInicial =G[nodoInicial]
    if len(camino) == (len(G)-1) and posicionFinal[nodoInicial]==True and posicionInicial[nodo]== True:
        return True

def esAdyacente(G,nodo1,nodo2):
    posicionNodo1 = G[nodo1]
    posicionNodo2 = G[nodo2]
    if posicionNodo1[nodo2] == True and posicionNodo2[nodo1] == True:
        return True

G = [
    [False,True,True,False,True],
    [True,False,True,True,False],
    [True,True,False,False,True],
    [False, True, False, False, True],
    [True,False, True, True, False]
]

listaAux = []
listaAux2 = []
nodoFinal = -1
#iterador = genCiclosHamiltoneanos1(G,0,listaAux,nodoFinal,0,listaAux2)
#print(next(iterador))

gen = genCiclosHamiltoneanos(G,0,[0],0)
print(list(gen))