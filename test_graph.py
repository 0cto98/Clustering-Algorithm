from graph import *

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
    