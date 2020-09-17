from math import sqrt

class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'


    def set_location(self, dx, dy):
        self.x = dx
        self.y = dy

    def distance_from_origin(self, dx, dy):
        return sqrt(self.x * self.x + self.y * self.y)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)
        
