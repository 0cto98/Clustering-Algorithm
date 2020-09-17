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
        l = 0
        if len(self.points)>=2:
            for i in range (len(self.points)-1):
                p0 = self.points[i]
                p1 = self.points[i+1]
                l += sqrt( ((p1.x-p0.x)**2)+((p1.y-p0.y)**2) )
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

def test_traj_lenght_1point():
    t=Trajectorie()
    p1=Point(0,0)
    t.add_point(p1)
    assert t.lenght()==0

def test_traj_lenght_gt2point():
    t=Trajectorie()
    p1=Point(0,0)
    p2=Point(1,0)
    p3=Point(1,4)
    t.add_point(p1)
    t.add_point(p2)
    t.add_point(p3)
    assert t.lenght()==5