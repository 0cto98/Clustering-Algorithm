import numpy as np
import pytest
from test_point import Point

class Trajectorie:
    #Create an empty Trajectorie
    def __init__(self):
        self.points = []

    #Return the point of index i
    def point_i(self,i):
        return self.points[i]

    #Add a Point at the end of the Trajectorie
    def add_point(self,P):
        self.points.append(P)
    
    #Add a Point at the index i of the Trajectorie
    def add_point_at_i(self,P,i):
        self.points.insert(i,P)

    #Return the lenght of the Trajectorie (i.e the sum of distance between each consecutive Point)
    def lenght(self):
        l = 0
        if len(self.points)>=2:
            for i in range (len(self.points)-1):
                p0 = self.points[i]
                p1 = self.points[i+1]
                l += np.sqrt( ((p1.x-p0.x)**2)+((p1.y-p0.y)**2) )
        return l

    #Return he number of Point of the Trajectorie
    def number_of_points(self):
        return len(self.points)

    #Print the Trajectorie
    def __str__(self):
        s = '<'
        for i in range(self.number_of_points()):
            s +=' '+str(self.point_i(i))
        s+=' >'
        return s

    def __eq__(self,other):
        return self.points == other.points


def test_traj_eq():
    t=Trajectorie()
    p1=Point(0,0)
    p2=Point(1,0)
    t.add_point(p1)
    t.add_point(p2)
    t2=Trajectorie()
    t2.add_point(p1)
    t2.add_point(p2)
    assert t == t2

def test_traj_different():
    t=Trajectorie()
    p1=Point(0,0)
    p2=Point(1,0)
    t.add_point(p1)
    t.add_point(p2)
    t2=Trajectorie()
    t2.add_point(p1)
    assert t != t2

def test_add_point_at_the_end():
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

def test_add_point_at_any_place():
    t=Trajectorie()
    p1=Point(0,0)
    p2=Point(1,0)
    p3=Point(5,0)
    t.add_point(p1)
    t.add_point(p2)
    t.add_point_at_i(p3,1)
    assert t.point_i(1).x==p3.x and t.point_i(1).y==p3.y

def test_num_of_points():
    t=Trajectorie()
    p1=Point(0,0)
    p2=Point(1,0)
    p3=Point(5,0)
    t.add_point(p1)
    t.add_point(p2)
    t.add_point(p3)
    assert t.number_of_points() == 3