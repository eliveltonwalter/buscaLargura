import math
from collections import deque

C = [ 'C1', 'C2', 'C3', 'C4', 'C5', 'C6']
L = [ ['C1', 'C4'], ['C1', 'C2'],
      ['C2', 'C1'], ['C2', 'C3'], ['C2', 'C5'], 
      ['C3', 'C2'],
      ['C4', 'C1'], ['C4','C6'],
      ['C5', 'C2'], ['C5','C6'],
      ['C6', 'C5'], ['C6', 'C4']]

#L = [['C4','C2'],['C1','C3','C5'], ['C2'], ['C1'], ['C2','C6'], ['C5']]

def main():
    N = generateGraph(C,L)
    source = 'C1'
    destination = 'C6'
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
    while currentPosition != source and currentPosition != None:
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
    graph = []
    for i in C:
        lstTmp = []
        for j in L:
            if( i == j[0] ):
                lstTmp.append(int(j[1][1])-1)
        graph.append(lstTmp)
    return graph
            

if __name__ == "__main__":
    main()
