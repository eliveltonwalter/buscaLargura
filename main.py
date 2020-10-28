from igraph import *
import math
from collections import deque

C = [ 'C1', 'C2', 'C3', 'C4', 'C5']
L = [['C4','C2'],['C1','C3','C5'], ['C2'], ['C1'], ['C2']]

def main():
    N = generateGraph(C,L)
    source = 'C1'
    destination = 'C5'
    p = shortestPath(N, source, destination)
    print(p)

def shortestPath(N, source, destination):
    intSource = int(source[1])-1
    intDestination = int(destination[1])-1
    Dv,Av = deepSearch(N, intSource)
    path = getPath(intSource,intDestination,Dv,Av)
    return path

def getPath(source,destination,Dv,Av):
    currentPosition = Av[destination]
    path = deque([])
    path.append(destination)
    while currentPosition != source:
        path.appendleft(currentPosition)
        currentPosition = Av[currentPosition]
    else:
        path.appendleft(currentPosition)
    return path
    
def deepSearch(N, s):
    #configurando todos os vértices
    Cv = []
    Dv = []
    Av = []
    for i in range(len(C)):
        Cv.append(False)
        Dv.append(math.inf)
        Av.append(None)
    #configurando o vértice de origem
    Cv[s] = True
    Dv[s] = 0
    #preparando a fila de visitas
    Q = deque([])
    Q.append(s)
    #Q.pop(s)
    #propagação das visitas
    while len(Q) > 0:
        u = Q.popleft()
        for v in N[u]:
            if(Cv[v] == False):
                Cv[v] = True
                Dv[v] = Dv[u]+1
                Av[v] = u
                Q.append(v)
    return Dv,Av

def generateGraph(C,L):
    g = Graph()
    g.add_vertices(len(C))
    matrixGraph = []
    N = [None]*len(C)
    for i, vI in enumerate(C):
        tempConections = []
        if(len(L[i]) > 0):
            for j, vJ  in L[i]:
                matrixGraph.append( (i,int(vJ)-1) )
                tempConections.append(int(vJ)-1)
        N[i] = tempConections
    g.add_edges(matrixGraph)
    plot(g, vertex_label=C, vertex_color="white")
    return N
            

if __name__ == "__main__":
    main()
