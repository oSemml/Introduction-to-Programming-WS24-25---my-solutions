import math

# Task 1: Function to compute angular distance and Euclidean distance
def ang_dist(x, y):
    # Compute the angle between two vectors x and y (in degrees) and their Euclidean distance
    angle = math.acos((x[0] * y[0] + x[1] * y[1]) / math.sqrt((x[0] ** 2 + x[1] ** 2) * (y[0] ** 2 + y[1] ** 2))) / math.pi * 180
    distance = math.sqrt((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    return angle, distance

# Task 2: Function to calculate the degree of a node in a graph
def node_degree(graph, node):
    # Return the degree of a node, which is the number of connections (edges) it has
    return len([1 for line in graph if node in line])

