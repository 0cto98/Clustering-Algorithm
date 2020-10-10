from test_point import Point

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

def test_add_edge():
    g = Graph()
    g.addEdge('a',1)
    assert g.edges == [('a',1)]

def test_count_edges():
    g = Graph()
    g.addEdge('a',1)
    g.addEdge('b',2)
    g.addEdge('c',3)
    g.addEdge('d',4)
    assert g.count_edges()==4

def test_graph_eq():
    g = Graph()
    g.addEdge('a',1)
    g.addEdge('b',2)
    g2 = Graph()
    g2.addEdge('b',2)
    g2.addEdge('a',1)
    assert g == g2

def test_graph_diff():
    g = Graph()
    g.addEdge('a',1)
    g.addEdge('b',2)
    g.addEdge('d',4)
    g2 = Graph()
    g2.addEdge('b',2)
    g2.addEdge('a',1)
    g2.addEdge('c',3)
    assert g != g2
    