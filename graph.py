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
        
        #for kruskal's algorhithm
        self.componentSet = []
        
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
    
    def updateEdge(self):
        self.e = {}
        for v in self.vertList.values():
            for edge, cost in v.connectedTo.items():
                self.e[cost] = (v, edge)
    
    def getVertices(self):
        return self.vertList.keys()
    
    def __iter__(self):
        return iter(self.vertList.values())
        
    def addEdge_undirect(self, f, t, cost = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.vertList[t].addNeighbor(self.vertList[f], cost)
        self.numEdges = self.numEdges + 1
    
    # For kruskle's algorhithm
    def check_component_cycle(self, f, t):
        '''for component in component set
        #   if f, t is in the same component
        #       discarded f, t
        #   else
        #       if f, or t is in one of component, then migrate
                the other together. Or create new component
        '''
        for component in self.componentSet:
            if f and t in component:
                print "Found Cycle !!"
                return True
        return False
    
    def merge_vertex_to_component(self, f, t):
        
        for component in self.componentSet:
            #if f | t in component:
            if f in component:
                component.append(t)
            if t in component:
                component.append(f)
                #break
            
            # what will happan if each vertex have their own component? 
        
        
        
        self.componentSet.append([f, t])
                
            

def traverse(y):
    x = y
    while(x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())
