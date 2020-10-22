from trajectorie import *

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