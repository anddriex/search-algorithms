from queue import Queue
from numpy import zeros
from graph import *
from aStarMaze import *

vertexMidPointsDict = createVertexMidPointsDict(createVertexDict(5,10))

def breadth_first(graph, goal, start=0):
    queue = Queue()
    queue.put(start)

    visited = zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if visited[vertex] == 1:
            continue
        
        if visited[goal - 1] != 1:
            draw_square(str(vertex + 1), vertexMidPointsDict)

        print("Visit: ", vertex + 1)
        visited[vertex] = 1

        for v in graph.get_adjacent_vertices(vertex):
            if visited[v] != 1 and visited[goal - 1] != 1:
                queue.put(v)

def depth_first(graph, visited, goal, current=0):
    if visited[current] == 1:
        return
    if visited[goal - 1] != 1:
        draw_square(str(current + 1), vertexMidPointsDict)
    visited[current] = 1
    print("Visit: ", current + 1)
    
    for vertex in graph.get_adjacent_vertices(current):
        if visited[goal - 1] != 1:
            depth_first(graph, visited, goal, vertex)
    
    
'''
g = AdjacencyMatrixGraph(9, directed=True)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 7)
g.add_edge(2, 4)
g.add_edge(2, 3)
g.add_edge(1, 5)
g.add_edge(5, 6)
g.add_edge(6, 3)
g.add_edge(3, 4)
g.add_edge(6, 8)

# breadth_first(g, 2)

visited = np.zeros(g.numVertices)
depth_first(g, visited)
'''