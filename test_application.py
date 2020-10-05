from test_clustering_algorithm import *
import pickle
import matplotlib.pyplot as plt

class Application:
    def __init__(self, path, grid_size):
        self.traj_list = import_data(path)
        self.grid_traj_list = grid_traj(self.traj_list, grid_size)
        self.centered_grid_traj_list = center_points_grid_cells(self.grid_traj_list, grid_size*2)
        self.graph = centered_grid_traj_list_to_graph(self.centered_grid_traj_list)
        pickle.dump(self.graph, open("graph", "wb"))

app = Application("C:/Users/tomri/Desktop/Master 1/Clustering-Algorithm/cabspottingdata",0.1)
g = pickle.load(open("graph", "rb"))
for edge in g.edges:
    x = [edge[0].x, edge[1].x]
    y = [edge[0].y, edge[1].y]
    plt.plot(x, y, c='r')
plt.savefig('Cluster.png') #Save the plot as .png file
plt.show()