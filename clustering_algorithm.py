from trajectorie import Trajectorie
from graph import Graph
from point import Point
import os
import csv



def grid_traj(traj_list, grid_size):
    """Take the list of trajectories A and return an other list of trajectories B so that every
    trajectorie which cross a square of the grid as a point in this square

    Args:
        traj_list ([list]): List of trajectories we want to cluster
        grid_size ([float]): Size of a grid's cell, the smaller it is, the more accurate the trajectories will be

    Returns:
        [list]: List of trajectories with one coordinate on every grid's cell it cross
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
    """Centers every point in the middle of the grid's square it is in
    It means thats all points in the same square will have the same
    coordinates so we'll be able to merge them in the next step

    Args:
        grid_traj_list ([list]): List of trajectories we want to cluster
        grid_size ([float]): Size of a grid's cell

    Returns:
        [list]: List of trajectories with coordinates center on grid's cell it is in
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
    """Construct the graph with the centered_grid_traj_list 
    Points with the same coordinates will be represented as a single node in the graph

    Args:
        centered_grid_traj_list ([list]): List of trajectories we want to cluster

    Returns:
        [list]: Graph of points from centered_grid_traj_list
    """
    g=Graph()
    for traj in centered_grid_traj_list:
        for i in range(traj.number_of_points()-1):
            p1=traj.point_i(i)
            p2=traj.point_i(i+1)
            if (p1 != p2):
                g.addEdge(p1, p2)
    return g


def import_data(directory):
    """Convert trajectories files - contained in a directory - to a list of Trajectories

    Args:
        directory ([string]): The directory containing trajectories files, must be in the same directory as the script

    Returns:
        [list]: list of Trajectories
    """
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