from graph import Graph, Vertex
from stack import Stack

vertStack = Stack()

def dfs(g, start):
    #dfsTree = Graph()
    currentVert = start
    
    if currentVert.getColor() == "white" :
        currentVert.setColor("black")
        vertStack.push(currentVert)
        print currentVert
        for nbr in currentVert.getConnections():
            if nbr.getColor() == "white":
                dfs(g, nbr)
        
    

print vertStack.items
        
    #return dfsTree
