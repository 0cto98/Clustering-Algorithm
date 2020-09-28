from math import sqrt

class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)

    def __eq__(self,other):
        return (self.x == other.x and self.y == other.y)

    def __hash__(self):
        return hash((self.x, self.y))

    def middle(self, other):
        return Point((self.x+other.x)/2,(self.y+other.y)/2)

def test_init():
    p = Point(1,2)
    assert p.x == 1 and p.y == 2

def test_distance():
    p1 = Point(1,1)
    p2 = Point(0,0)
    assert p1.distance(p2) == sqrt(2)

def test_eq():
    p1 = Point(1,1)
    p2 = Point(1,1)
    assert p1 == p2

def test_middle():
    p1 = Point(0,0)
    p2 = Point(1,1)
    p3 = Point(0.5,0.5)
    assert p1.middle(p2) == p3

        
