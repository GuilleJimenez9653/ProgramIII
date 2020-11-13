#Taller 1 
#Busca todos los ciclos Hamiltoneanos de un grafo
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

#Comprueba que el ciclo es Hamiltoneano
def esHamiltoneano(G,camino,nodo,nodoInicial):
    posicionFinal = G[nodo]
    posicionInicial =G[nodoInicial]
    if len(camino) == (len(G)-1) and posicionFinal[nodoInicial]==True and posicionInicial[nodo]== True:
        return True
    else:
        return False

#Comprueba que dos vertices del grafo son adyacentes
def esAdyacente(G,nodo1,nodo2):
    posicionNodo1 = G[nodo1]
    posicionNodo2 = G[nodo2]
    if posicionNodo1[nodo2] == True and posicionNodo2[nodo1] == True:
        return True
    else:
        return False

G = [
    [False,True,True,False,True],
    [True,False,True,True,False],
    [True,True,False,False,True],
    [False, True, False, False, True],
    [True,False, True, True, False]
]

gen = genCiclosHamiltoneanos(G,0,[0],0)
print(list(gen))