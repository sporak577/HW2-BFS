import networkx as nx

#need to import pythons queue module (tipp from chatgpt)
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        #initializing a queue
        Q = deque([start])
        #using a set because it only allows unique elements, no duplicates. faster processing. 
        visited = {start}
        #Q.append() is used from deque module
        #dictionary where each node stores the parent node from which it was discovered
        parent = {start: None}
       
       
        while Q:
            #removes the first (oldest) element that was added to the queue, that's why it's called first in first out
            v = Q.popleft()

            if end is not None and v == end: 
                #end node input and path doesn't exist, as self is it's only neighbor
                path = []
                while v is not None: 
                    path.append(v)
                    v = parent[v]
                return path[::-1]

            #accessing the adjacency list of the graph, get neighbors of the graph
            N = self.graph[v]
            print(N)

            #checking
            print(N)
            for node in N:
                if node not in visited: 
                    visited.add(node)
                    parent[node] = v #tracks where we came from
                    #add an element to the queue
                    Q.append(node)

        #if BFS did not find a path to the end node return None (e.g. end is not in the graph)
        #if no end node defined convert visited set into a list and return BFS traverse
        return None if end else list(visited)




