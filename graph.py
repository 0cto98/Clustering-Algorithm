from point import *

class Graph:
    
    graph_dict={}
    
    def addEdge(self,node,neighbour):  
        if node not in self.graph_dict:
            self.graph_dict[node]=[neighbour]
        else:
            self.graph_dict[node].append(neighbour)
            
    def show_edges(self):
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                print("(",node,", ",neighbour,")")
            

g= Graph()
g.addEdge(Point(0,0), Point(1,1))
g.addEdge(Point(0,0), Point(1,2))
g.addEdge(Point(1,1), Point(1,2))
g.addEdge(Point(1,1), Point(4,4))
g.show_edges()