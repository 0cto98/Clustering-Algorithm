import numpy as np
import pytest
from point import Point

class Trajectorie:
    #Create an empty Trajectorie
    def __init__(self):
        self.points = []

    #Return the point of index i
    def point_i(self,i):
        return self.points[i]

    #Add a Point at the end of the Trajectorie
    def add_point(self,P):
        self.points.append(P)
    
    #Add a Point at the index i of the Trajectorie
    def add_point_at_i(self,P,i):
        self.points.insert(i,P)

    #Return the lenght of the Trajectorie (i.e the sum of distance between each consecutive Point)
    def lenght(self):
        l = 0
        if len(self.points)>=2:
            for i in range (len(self.points)-1):
                p0 = self.points[i]
                p1 = self.points[i+1]
                l += np.sqrt( ((p1.x-p0.x)**2)+((p1.y-p0.y)**2) )
        return l

    #Return he number of Point of the Trajectorie
    def number_of_points(self):
        return len(self.points)

    #Print the Trajectorie
    def __str__(self):
        s = '<'
        for i in range(self.number_of_points()):
            s +=' '+str(self.point_i(i))
        s+=' >'
        return s

    def __eq__(self,other):
        return self.points == other.points