from point import Point

class Graph:
    """self.dict = { A : [B, C]
                     B : [A]
                     C : []
                   }
        self.nodes = [A, B, C]
        self.edges = [(A, B), (A, C), (B, A)]
    """
    def __init__(self):
        self.dict={}
        self.nodes=[]
        self.edges=[]

    
    def addEdge(self,node,neighbour):  
        if node not in self.dict:
            self.dict[node]=[neighbour]
        else:
            self.dict[node].append(neighbour)
        if neighbour not in self.dict:
            self.dict[neighbour]=[]
        
        if node not in self.nodes:
            self.nodes.append(node)
        if neighbour not in self.nodes:
            self.nodes.append(neighbour)
        
        self.edges.append((node,neighbour))

    def count_edges(self):
        return len(self.edges)
    
    def __eq__(self,other):
        """Two graphs are equal if they have the same edges, no matter the order"""
        return set(self.edges) == set(other.edges)
    
    #---Debugging methods---
    def show_edges(self):
        for edge in self.edges:
            a, b = edge
            print('( '+str(a)+' , '+str(b)+' )')

    def show_nodes(self):
        for node in self.nodes:
            print(node)

    def show_dict(self):
        print(self.dict)