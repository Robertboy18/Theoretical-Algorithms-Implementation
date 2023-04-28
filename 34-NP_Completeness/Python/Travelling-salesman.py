import random
import math
import copy
import time

# Function to calculate the distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Function to calculate the cost of the path
def cost(path, distances):
    pathCost = 0
    for i in range(len(path)):
        if i == len(path) - 1:
            pathCost += distances[path[i]][path[0]]
        else:
            pathCost += distances[path[i]][path[i + 1]]
    return pathCost

# Function to swap two cities in a path
def swap(a, b):
    temp = a
    a = b
    b = temp
    return a, b

# Function to find the best neighbour
def bestNeighbour(path, distances):
    bestNeighbour = copy.deepcopy(path)
    bestCost = cost(path, distances)
    for i in range(len(path)):
        for j in range(i + 1, len(path)):
            newPath = copy.deepcopy(path)
            newPath[i], newPath[j] = swap(newPath[i], newPath[j])
            newCost = cost(newPath, distances)
            if newCost < bestCost:
                bestNeighbour = copy.deepcopy(newPath)
                bestCost = newCost
    return bestNeighbour, bestCost

# Function to find the best path
def bestPath(path, distances, maxIterations):
    bestPath = copy.deepcopy(path)
    bestCost = cost(path, distances)
    for i in range(maxIterations):
        newPath, newCost = bestNeighbour(bestPath, distances)
        if newCost < bestCost:
            bestPath = copy.deepcopy(newPath)
            bestCost = newCost
    return bestPath, bestCost

# Function to generate a random path
def randomPath(path):
    for i in range(len(path)):
        swapWith = int(random.random() * len(path))
        path[i], path[swapWith] = swap(path[i], path[swapWith])
    return path