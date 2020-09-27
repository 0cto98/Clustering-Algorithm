from test_TDD_trajectorie import *
from graph import *

def clustering_algorith(traj_list):
    g= Graph()
    for traj in traj_list:
        for i in range (len(traj.points)-1):
            g.addEdge(traj.point_i(i),(traj.point_i(i+1)))
    return g


def test_single_traj():
    t=Trajectorie()
    t.add_point(Point(0,0))
    t.add_point(Point(1,0))

    g= Graph()
    g.addEdge(Point(0,0), Point(1,0))

    assert clustering_algorith([t]) == g
