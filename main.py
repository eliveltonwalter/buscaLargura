from igraph import *
import math
from collections import deque

C = [ 'C1', 'C2', 'C3', 'C4', 'C5']
L = [['C4','C2'],['C3','C5'], [], [], []]

def main():
    adjacentMatrix = generateGraph(C,L)
    source = 'C1'
    destination = 'C5'
    p = shortestPath(adjacentMatrix, source, destination)

def shortestPath(adjacentMatrix, source, destination):
    intSource = int(source[1])
    intDestination = int(source[1])
    pathMatrix = deepSearch(adjacentMatrix, intSource)
    return pathMatrix

def deepSearch(adjacentMatrix, s):
    #configurando todos os vértices
    Cv = []
    Dv = []
    Av = []
    for i in range(len(C)-1):
        Cv.append(False)
        Dv.append(math.inf)
        Av.append(None)
    #configurando o vértice de origem
    Cv[0] = True
    Dv[0] = 0
    #preparando a fila de visitas
    C.pop(s)
    Q = deque(C)
    #Q.pop(s)
    #propagação das visitas
    while len(Q) > 0:
        u = Q.popleft()
        for i, v in enumerate(adjacentMatrix):
            print(i)
            print(v)
        else:
            break
    return Dv,Av

def generateGraph(C,L):
    g = Graph()
    g.add_vertices(len(C))
    matrixGraph = []
    vectorConections = [None]*len(C)
    for i, vI in enumerate(C):
        if(len(L[i]) > 0):
            tempConections = []
            for j, vJ  in L[i]:
                matrixGraph.append( (i,int(vJ)-1) )
                tempConections.append(int(vJ)-1)
        vectorConections[i] = tempConections
    print(matrixGraph)
    print(vectorConections)
    g.add_edges(matrixGraph)
    plot(g, vertex_label=C, vertex_color="white")
    return matrixGraph
            

if __name__ == "__main__":
    main()
