from graph import *
from bfs import bfs
from dfs import dfs
from kruskal import *

def main():
    g = Graph()
    
    g.addEdge_undirect(0, 5, 10)
    g.addEdge_undirect(0, 1, 28)
    g.addEdge_undirect(1, 6, 14)
    g.addEdge_undirect(1, 2, 16)
    g.addEdge_undirect(5, 4, 25)
    g.addEdge_undirect(4, 3, 22)
    g.addEdge_undirect(3, 2, 12)
    g.addEdge_undirect(4, 6, 24)
    g.addEdge_undirect(3, 6, 18)
    
    return g

ng = main()
st = Kruskal(ng)
st.updateEdge()
print st.e
