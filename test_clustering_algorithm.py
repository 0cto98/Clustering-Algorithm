from test_TDD_trajectorie import *
from graph import *


#Take the list of trajectories A and return an other list of trajectories B so that every trajectorie which cross a square of the grid as a point in this square
def grid_traj(traj_list, grid_size):    
    grid_traj_list = []
    for traj in traj_list:
        t = Trajectorie()
        for i in range(traj.number_of_points()-1):
            p1=traj.point_i(i)
            t.add_point(p1)
            p2=traj.point_i(i+1)
            if(p1.distance(p2)>grid_size):
                pass
                

"""
def test_grid_single_traj():
    t=Trajectorie()
    t.add_point(Point(0,0))
    t.add_point(Point(1,0))

    t2=Trajectorie()
    t2.add_point(Point(0,0))
    t2.add_point(Point(0.5,0.5))
    t2.add_point(Point(1,1))

    assert grid_traj([t],0.5) == [t2]
"""
