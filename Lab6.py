##CS 2302 Data Structures
##Instructor:Diego Aguirre
##TA: Anindita Nath
##Project 6 Option B
##Modified and submitted by Andres Ponce 80518680
##Date of last modification 12/4/2018
##Purpose: Implement Kruskal's algorithm and Topological sort.
##Graphs implementation used. 

import os
import random
import time
import re
import math

from Graphs.GraphAM import GraphAM
from Graphs.GraphAL import GraphAL
####################   Kruskal's algorithm/Topological sort    ######################

## Kruskal's algorithm (Minimum Spanning Tree)
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent,parent[i])

def union(parent,rank,x,y):
    find1=find(parent,x)
    find2=find(parent,y)

    if rank[find1]<rank[find2]:
        parent[find1] = find2
    elif rank[find1]>rank[find2]:
        parent[find2]=find1
    else:
        parent[find2]=find1
        rank[find1]+=1
        
def kruskalMST(graph):
    vertices = graph.get_num_vertices()
    MST = []
    edges = []
    for i in range (vertices):
        for j in range (vertices):
            if graph.adj_matrix[i][j] !=0 and (j,i) not in edges:
                k = graph.adj_matrix[i][j]
                edges.append([i,j,k])
    sorted_edges = sorted(edges, key=lambda e:graph.adj_matrix[e[0]][e[1]])
    
    parent = []
    rank = []
    for i in range(vertices):
        parent.append(i)
        rank.append(0)
    e=0
    i=0
    while e<vertices-1:
        u,v,w=sorted_edges[i]
        i=i+1
        x=find(parent,u)
        y=find(parent,v)
        if x != y:
            e=e+1
            MST.append([u,v,w])
            union(parent,rank,x,y)
    return MST
    for u,v,weight in MST: 
        print (str(u) + " -- " + str(v) + " == " + str(weight))
        #print ("%d -- %d == %d" % (u,v,weight))
        

        
### Topological sort ##
def topological_sort(graph):
    visited = [False]*graph.get_num_vertices()
    stack = []

    for item in range(graph.get_num_vertices()):
        if visited[item] == False:
            topologicalSortRec(graph,item,visited,stack)

    return stack

def topologicalSortRec(graph,v,visited,stack):
    visited[v] = True
    for item in graph.get_vertices_reachable_from(v):
        if visited[item] == False:
            topologicalSortRec(graph,item,visited,stack)

    stack.insert(0,v)

graphAM = GraphAM(initial_num_vertices=11, is_directed=True)
graphAM.add_edge(0, 1, 2)
graphAM.add_edge(0, 2, 3)
graphAM.add_edge(0, 3, 4)
graphAM.add_edge(1, 4, 2)
graphAM.add_edge(2, 5, 2)
graphAM.add_edge(3, 6, 5)
graphAM.add_edge(4, 7, 1)
graphAM.add_edge(5, 8, 3)
graphAM.add_edge(6, 9, 8)
graphAM.add_edge(7, 10, 5)
graphAM.add_edge(8, 10, 6)
graphAM.add_edge(9, 10, 2)
#   /--> 1 -> 4 -> 7 -\
#  /                   \
# 0 -> 2 -> 5 -> 8------> 10
#  \                   /
#   \--> 3 -> 6 -> 9--/
print ("Topological sort: ", topological_sort(graphAM))
print('Kruskal MST: ')
MST=kruskalMST(graphAM)
for u,v,weight in MST: 
        print ("From " + str(u) + " to " + str(v) + " weight is " + str(weight))

