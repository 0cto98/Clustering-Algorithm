from test_clustering_algorithm import *
import pickle
import matplotlib.pyplot as plt
import numpy as np
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

class Application:
    def __init__(self, path, grid_size):
        """Process the whole clustering algorithm on a set of trajectories files:
        Convert trajectories files to a list of Trajectorie objects
        Apply the grid_traj() function in order to have at least one Point on every grid's cell it cross
        Center every Point on the middle of grid's cell it belongs
        Convert the list of Trajectories to a Graph, which has the effect of merging Points that are in the same cell
        Save the graph if we want to re-use it without having to re-compute everything
        Plot the base trajectories
        Plot the clustered trajectories

        Args:
            path ([string]): Path to the directory containing trajectories files
            grid_size ([float]): Size of grid's cells, used in grid_traj() and center_points_grid_cells() functions
        """
        self.traj_list = import_data(path)
        self.grid_traj_list = grid_traj(self.traj_list, grid_size)
        self.centered_grid_traj_list = center_points_grid_cells(self.grid_traj_list, grid_size)
        self.graph = centered_grid_traj_list_to_graph(self.centered_grid_traj_list)
        pickle.dump(self.graph, open(str(dir_path)+"/graph", "wb"))
        self.show_base_traj()
        self.show_crustered_traj()
        plt.show()

    def show_base_traj(self):
        plt.figure(1)
        for traj in self.traj_list:
            l = int(traj.number_of_points())
            x, y = [], []
            for i in range (l):
                p = traj.point_i(i)
                x.append(p.x)
                y.append(p.y)
            plt.plot(x,y)
        plt.axis('equal')
        plt.xlim(37.3, 38.1)
        plt.ylim(-122.6, -121.9)
        plt.savefig(str(dir_path)+'/Base_Trajecories.png') #Save the plot as .png file
        plt.grid(True)

    def show_crustered_traj(self):
        plt.figure(2)
        g = pickle.load(open(str(dir_path)+"/graph", "rb"))
        for edge in g.edges:
            x = [edge[0].x, edge[1].x]
            y = [edge[0].y, edge[1].y]
            plt.plot(x, y, c='r')
        plt.axis('equal')
        plt.xlim(37.3, 38.1)
        plt.ylim(-122.6, -121.9)
        plt.savefig(str(dir_path)+'/Cluster.png') #Save the plot as .png file
        plt.grid(True)

app = Application(str(dir_path)+"/cabspottingdata",0.05)

