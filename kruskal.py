"""
kruskal's Algorithm

input: Graph()
output: minimum spanning tree (graph)

"""
from graph import Graph, Vertex

def Kruskal(g):
    # Iinit Spanning Tree - T
    T = Graph()
    for i in range(g.numVertices):
        T.addVertex(i)
    
    T.e = g.e # copy an edge set from g
    
    # For cost in T.e
    # //T.e already sorted by value!
    for cost in T.e.keys():
        v1, v2 = T.e.pop(cost)
        
        # Check if the edge will make cycle
        # if hasCycle(v1, v2):
        #   break
        # T.addEdge(v1, v2, cost)
