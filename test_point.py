from point import *

def test_init():
    p = Point(1,2)
    assert p.x == 1 and p.y == 2

def test_distance():
    p1 = Point(1,1)
    p2 = Point(0,0)
    assert p1.distance(p2) == np.sqrt(2)

def test_eq():
    p1 = Point(1,1)
    p2 = Point(1,1)
    assert p1 == p2

def test_middle():
    p1 = Point(0,0)
    p2 = Point(1,1)
    p3 = Point(0.5,0.5)
    assert p1.middle(p2) == p3

        
