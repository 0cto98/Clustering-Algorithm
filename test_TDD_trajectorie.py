import math
import pytest
from point import *

#trajectorie lenght
class Trajectorie:
    def __init__(self):
        self.points = []

    def add_point(self,P):
        self.points.append(P)

    def lenght(self):
        p0 = self.points[0]
        p1 = self.points[1]
        l = sqrt( ((p1.x-p0.x)**2)+((p1.y-p0.y)**2) )
        return l


def test_traj_init():
    t = Trajectorie()
    assert t != None

def test_add_point():
    t=Trajectorie()
    p1=Point(0,0)
    t.add_point(p1)
    assert p1 in t.points

def test_traj_lenght_2points():
    t=Trajectorie()
    p1=Point(0,0)
    p2=Point(1,0)
    t.add_point(p1)
    t.add_point(p2)
    assert t.lenght()==1
