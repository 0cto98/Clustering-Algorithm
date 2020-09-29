from test_TDD_trajectorie import Trajectorie
from graph import Graph
from point import Point


#Take the list of trajectories A and return an other list of trajectories B so that every trajectorie which cross a square of the grid as a point in this square
def grid_traj(traj_list, grid_size):    
    grid_traj_list = []
    for traj in traj_list:
        t = traj
        traj_modified = True    #we stop the while loop once we went through the whole traj without adding intermediate point, initialized to True so the loop runs at least once
        while traj_modified:
            traj_modified = False  #we start going through the traj, but for now we modified nothing
            for i in range(t.number_of_points()-1):
                p1=t.point_i(i)
                p2=t.point_i(i+1)
                if(p1.distance(p2)>grid_size):
                    traj_modified = True  #we add a point
                    t.add_point_at_i(p1.middle(p2),i+1)
        grid_traj_list.append(t)
    return grid_traj_list
                
                

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

g = grid_traj([t2,t],0.5)
for i in range (len(g)):
    print(g[i])


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
       
