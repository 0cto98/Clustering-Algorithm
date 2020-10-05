from test_TDD_trajectorie import Trajectorie
from test_graph import Graph
from test_point import Point



def grid_traj(traj_list, grid_size):
    """
    Take the list of trajectories A and return an other list of trajectories B so that every
    trajectorie which cross a square of the grid as a point in this square
    Args:
        traj_list [list]: List of trajectories we want to cluster
        grid_size [int] : Size of a grid's cell, the smaller it is, the more accurate the trajectories will be
    Return:
        grid_traj_list [list] : List of trajectories with one coordinate on every grid's cell it cross
    """
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


def center_points_grid_cells(grid_traj_list, grid_size):
    """
    Centers every point in the middle of the grid's square it is in
    It means thats all points in the same square will have the same
    coordinates so we'll be able to merge them in the next step
    Args:
        grid_traj_list [list]: List of trajectories we want to cluster
        grid_size [int] : Size of a grid's cell
    Return:
        grid_traj_list [list] : List of trajectories with coordinates center on grid's cell it is in
    """
    centered_grid_traj_list = []
    for traj in grid_traj_list:
        t = Trajectorie()
        for i in range(traj.number_of_points()):
            point=traj.point_i(i)
            x = point.x - point.x%grid_size + grid_size/2
            y = point.y - point.y%grid_size + grid_size/2
            t.add_point(Point(x,y))
        centered_grid_traj_list.append(t)
    return centered_grid_traj_list


def centered_grid_traj_list_to_graph(centered_grid_traj_list):
    """
    Construct the graph with the centered_grid_traj_list 
    Points with the same coordinates will be represented as a single node in the graph
    Args:
        centered_grid_traj_list [list]: List of trajectories we want to cluster
    Return:
        g [list] : Graph of points from centered_grid_traj_list
    """
    g=Graph()
    for traj in centered_grid_traj_list:
        for i in range(traj.number_of_points()-1):
            p1=traj.point_i(i)
            p2=traj.point_i(i+1)
            if (p1 != p2):
                g.addEdge(p1, p2)
    return g


import os
import csv
def import_data(directory):
    traj = []
    for file in os.listdir(directory):
        t = Trajectorie()
        with open(str(directory)+'/'+str(file), newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                line = row[0].split()
                p = Point(float(line[0]),float(line[1]))
                t.add_point(p)
        traj.append(t)
    return traj


"""
traj = import_data("C:/Users/tomri/Desktop/Master 1/Clustering-Algorithm/cabspottingdata")
print(traj[0])


t = Trajectorie()
p1=Point(0.1,0.1)
p2=Point(5.1,0.1)
t.add_point(p1)
t.add_point(p2)
t2 = Trajectorie()
p1=Point(0.8,0.8)
p2=Point(5.8,0.8)
t2.add_point(p1)
t2.add_point(p2)

print(t)
print(t2)
print("---")
size = 1
g = grid_traj([t2,t],size)
for i in range (len(g)):
    print(g[i])

print("---")

g = center_points_grid_cells(g,size)
for i in range (len(g)):
    print(g[i])
print("---")
g = centered_grid_traj_list_to_graph(g)
g.show_edges()
print("---")
g.show_nodes()
print("---")
g.show_dict()
"""

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
       
