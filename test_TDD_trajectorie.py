import math
import pytest
from point import *

#trajectorie lenght
class Trajectorie:
    def __init__(self):
        self.points = []

    def add_point(self,P):
        self.points.append(P)


def test_traj_init():
    t = Trajectorie()
    assert t != None

def test_add_point():
    t=Trajectorie()
    p1=Point(0,0)
    t.add_point(p1)
    assert p1 in t.points