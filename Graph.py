
from Node import Node
from Graph import Graph

class Graph:
    def __init__(self,name=None,direcionado=False):
        if(name)
            self.name = name
        else:
            self.name = "Graph"
        self.graph = {}

    def add_edge(self,node1,node2):
        pass

    def add_node(self,index=None):
        n = Node(index)
        self.graph[n] = {};
        return n

    def remove_edge(self,edge):
        pass

    def remove_node(self,node):
        pass

    def max_weight(self,departure,arrival):
        pass

    def min_weight(self,departure,arrival):
        pass

    def most_connected(self):
        pass

    def least_connected(self):
        pass