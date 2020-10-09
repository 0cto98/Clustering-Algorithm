import numpy as np

class Point:
    #Initialize the Point with coordinates (x,y)
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    #Print the Point(usefull for debugging)
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    #Return the distance between two Points
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return np.sqrt(dx * dx + dy * dy)

    def __eq__(self,other):
        return (self.x == other.x and self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    #Return the middle Point between two Points
    def middle(self, other):
        return Point((self.x+other.x)/2,(self.y+other.y)/2)



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

        
