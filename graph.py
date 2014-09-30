class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white" #default color is white.
        
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight
    
    def __str__(self):
        return str(self.id) + " connectedTO: " + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getId(self):
        return self.id
        
    def getWeight(self, nbr):
        return self.connectedTo[nbr]
    
    def setColor(self, color):
        self.color = color
    
    def getColor(self):
        return self.color
    
    def setDistance(self, distance):
        self.distance = distance
    
    def getDistance(self):
        return self.distance
        
    def setPred(self, pred):
        self.pred = pred
    
    def getPred(self):
        return self.pred
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.numEdges = 0
        
    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.numEdges = self.numEdges + 1
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())

def main():
    g = Graph()
    total_vertice = 7
    
    for i in range(total_vertice + 1):
        g.addVertex(i)
    
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    g.addEdge(3, 7)
    g.addEdge(4, 7)
    g.addEdge(5, 7)
    g.addEdge(6, 7)
    
    return g
    
if __name__ == "__main__":
    main()
