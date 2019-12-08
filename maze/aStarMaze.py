# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 13:22:14 2019

@author: edwin
"""


import turtle as t
from numpy import cumsum
import maze

class Graph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, id):
        return self.edges[id]

    def cost(self, from_node, to_node):
        return self.weights[(from_node, to_node)]
        

def heuristic(id):
    """
    Builds Maze heuristic
    """
    H = {
        '1': 29,
        '2': 30,
        '3': 31,
        '4': 14,
        '5': 13,
        '6': 12,
        '7': 11,
        '8': 10,
        '9': 9,
        '10': 8,
        '11': 28,
        '12': 33,
        '13': 32,
        '14': 15,
        '15': 16,
        '16': 13,
        '17': 12,
        '18': 15,
        '19': 6,
        '20': 7,
        '21': 27,
        '22': 26,
        '23': 27,
        '24': 28,
        '25': 17,
        '26': 18,
        '27': 13,
        '28': 14,
        '29': 5,
        '30': 6,
        '31': 24,
        '32': 25,
        '33': 26,
        '34': 19,
        '35': 18,
        '36': 19,
        '37': 20,
        '38': 3,
        '39': 4,
        '40': 5,
        '41': 23,
        '42': 22,
        '43': 21,
        '44': 20,
        '45': 19,
        '46': 20,
        '47': 3,
        '48': 2,
        '49': 1,
        '50': 0
    }

    return H[id]
    
def createVertexDict(rows,cols):
    c = 0
    vertexDict = {}
    for i in range(rows):
        for j in range(cols):
            c += 1
            vertexDict[str(c)] = (i,j)
    return vertexDict

def createVertexMidPointsDict(vertexDict):
    vertexMidPointList = {}
    for v in vertexDict:
        pos = vertexDict[v]
        x = -190 + ((pos[1]*28) + 14)
        y =  160 - ((pos[0]*28 ) + 14)
        vertexMidPointList[str(v)] = (x,y)
    return vertexMidPointList

def get_weights(edges):
    weights = {}
    for vertex, connected in edges.items():
        for n in connected:
            weights[(vertex, n)] = 1
    return weights

def draw_square(node_id, vertexMidPointsDict, color="medium sea green", scale=1, 
    correction=500, ts=None, text=None):
    """
    Draw a square in turtle over the map background to 
    indicate the exapnsion of the search and the shortest path
    node_id: the corresponding node in the graph (city)
    correction: corrects the origin of the geo_pos pixels
    ts: a turtle object can be passed to the function, 
    if not a turtle object is created
    To animante the shortest path a single turtle object is 
    define outside the function and passed as parameter
    """
    if ts == None:
        ts = t.Turtle(shape="square")
    ts.shapesize(0.5, 0.5)
    ts.color(color)
    ts.penup()
    x, y = vertexMidPointsDict[node_id]
    ts.goto(x, y)
    if text != None:
        ts.write(str(text), font=("Arial", 20, "normal"))


def pathfromOrigin(origin, n, parents):
    # Builds shortest path from search result (parents)
    if origin == n:
        return []

    pathO = [n]
    i = n

    while True:
        i = parents[i]
        pathO.insert(0, i)
        if i == origin:
            return pathO


def costofPath(path, graph):
    # Returns the cumulated cost of path
    cum_costs = [0]
    for i in range(len(path)-1):
        cum_costs += [graph.cost(path[i], path[i+1])]

    return cumsum(cum_costs)
    
def getF(oL):
    """
    Returns costs of queue F = C + H
    C: cost of route
    H: heuristic cost 
    """
    return [i[1] for i in oL]


def findleastF(oL):
    """
    finds the node with least F in oL (queue)
    This is equivalent to build a priority queue
    """
    mF = min(getF(oL))
    for ni in range(len(oL)):
        if oL[ni][1] == mF:
            return oL.pop(ni)[0]


def aStar(graph, vertexMidPointsDict, start, goal):
    openL = []
    openL.append((start, 0))
    parents = {}
    costSoFar = {}
    parents[start] = None
    costSoFar[start] = 0

    while bool(len(openL)):
        current = findleastF(openL)
        draw_square(current, vertexMidPointsDict)  # Draw search expansion

        if current == goal:
            break

        for successor in graph.neighbors(current):
            newCost = costSoFar[current] + graph.cost(current, successor)
            if successor not in costSoFar or newCost < costSoFar[successor]:
                costSoFar[successor] = newCost
                priority = newCost + heuristic(successor)
                openL.append((successor, priority))
                parents[successor] = current

        print('open list',openL)

    return parents


def main(argv):
    """
    Usage:
      python graphMaze.py
      Final point the exit of the maze
      Start point:  the enter of the maze

    Example:
      python graphMaze.py
    """

    startPoint = '1'

    endPoint = '50'

    maze_graph = Graph()  # Builds a Graph

    # Adding edges (adjacency list)
    maze_graph.edges = {
        '1': ['2', '11'],
        '2': ['1', '3'],
        '3': ['2', '13'],
        '4': ['5', '14'],
        '5': ['4', '6'],
        '6': ['5', '7', '16'],
        '7': ['6', '8', '17'],
        '8': ['7', '9'],
        '9': ['8', '10'],
        '10': ['9', '20'],
        '11': ['1', '21'],
        '12': ['13'],
        '13': ['3', '12'],
        '14': ['4', '15'],
        '15': ['14', '25'],
        '16': ['6', '17'],
        '17': ['7', '16', '27'],
        '18': ['28'],
        '19': ['20', '29'],
        '20': ['10', '19'],
        '21': ['11', '22'],
        '22': ['21', '32'],
        '23': ['24', '33'],
        '24': ['23'],
        '25': ['15', '26', '35'],
        '26': ['25', '36'],
        '27': ['17', '28'],
        '28': ['18', '27'],
        '29': ['19', '39'],
        '30': ['40'],
        '31': ['32', '41'],
        '32': ['22', '31', '33'],
        '33': ['23', '32'],
        '34': ['35', '44'],
        '35': ['25', '34', '45'],
        '36': ['26', '37'],
        '37': ['36'],
        '38': ['39', '48'],
        '39': ['29', '38', '40'],
        '40': ['30', '39'],
        '41': ['31', '42'],
        '42': ['41','43'],
        '43': ['42','44'],
        '44': ['34','43'],
        '45': ['35','46'],
        '46': ['45'],
        '47': ['48'],
        '48': ['38','47', '49'],
        '49': ['48','50'],
        '50': ['49']
    }

    # Adding weights to edges
    maze_graph.weights = get_weights(maze_graph.edges)
    
    vertexMidPointsDict = createVertexMidPointsDict(createVertexDict(5,10))

    # Building aStar path of parents
    parents = aStar(maze_graph, vertexMidPointsDict, startPoint, endPoint)

    # Calculating and printing the shortest path
    shortest_path = pathfromOrigin(startPoint, endPoint, parents)
    print('shortest path', shortest_path)

    # Calculating the cost of the shortest path
    cost_tsp = costofPath(shortest_path, maze_graph)

    # Draw shortest path 
    for ni in shortest_path:
        draw_square(ni, vertexMidPointsDict, color="salmon")

    # Animate shortest path agent and include cost
    tsp = t.Turtle(shape="square")

    for i, ni in enumerate(shortest_path):
        draw_square(ni, vertexMidPointsDict, color="dodger blue", ts=tsp, text=cost_tsp[i])

    t.exitonclick()  # Al hacer clic sobre la ventana grafica se cerrara


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])
