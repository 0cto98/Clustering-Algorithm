from clustering_algorithm import *

def test_grid_single_traj():
    t=Trajectorie()
    t.add_point(Point(0,0))
    t.add_point(Point(1,0))
    t2=Trajectorie()
    t2.add_point(Point(0,0))
    t2.add_point(Point(0.5,0))
    t2.add_point(Point(1,0))
    g=grid_traj([t],0.5)
    assert g == [t2]

def test_grid_multiple_traj():
    t = Trajectorie()
    p1=Point(0,0)
    p2=Point(2,0)
    t.add_point(p1)
    t.add_point(p2)
    t2 = Trajectorie()
    p1=Point(1,1)
    p2=Point(2,2)
    t2.add_point(p1)
    t2.add_point(p2)
    
    result_t = Trajectorie()
    result_t.add_point(Point(1,1))
    result_t.add_point(Point(1.25,1.25))
    result_t.add_point(Point(1.5,1.5))
    result_t.add_point(Point(1.75,1.75))
    result_t.add_point(Point(2,2))
    result_t2 = Trajectorie()
    result_t2.add_point(Point(0,0))
    result_t2.add_point(Point(0.5,0.0))
    result_t2.add_point(Point(1.0,0.0))
    result_t2.add_point(Point(1.5,0.0))
    result_t2.add_point(Point(2,0))
        
    g = grid_traj([t2,t],0.5)

    assert g == [result_t,result_t2]
       
