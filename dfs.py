from graph import Graph, Vertex
from stack import Stack

vertStack = Stack()

def dfs(g, start):
    #dfsTree = Graph()
    start.setDistance(0)
    start.setPred(None)
    vertStack = Stack()
    vertStack.push(start)
    
    while(vertStack.size() > 0):
        currentVert = vertStack.pop()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "white":
                nbr.setColor("grey")
                nbr.setDistance(currentVert.getDistance() + 1)
                vertStack.push(nbr)
        print currentVert.getId()
        currentVert.setColor('black')
    

    #return dfsTree
