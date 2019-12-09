# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 21:48:42 2019

@author: edwin
"""
import numpy as np

from traversal import *



edges = {
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


g = AdjacencyMatrixGraph(50)

for v, i in edges.items():
    for adjacency_v in i:
        g.add_edge(int(v) - 1, int(adjacency_v) - 1)
#print(g.get_adjacent_vertices(24))
breadth_first(g, 50)

"""
def get_short_path(steps_take):
    for s in steps_take:
        current_h = heuristic(str(s + 1))
        best_h = current_h
        if current_h <= best_h:
"""            
#for vertex, index in vertices:
 #   print(vertex, index)
