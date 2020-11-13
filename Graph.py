
from Node import Node
from Edge import Edge

class Graph:
    def __init__(self,name=None,direcionado=False):
        if name:
            self.name = name
        else:
            self.name = "Graph"
        self.direcionado=direcionado
        self.nodes=[]
        self.edges=[]

    def add_edge(self,node1,node2):
        e = Edge(node1,node2,1,None,self.direcionado)
        if self.direcionado == False:
            node1.add_edge(e)
            node2.add_edge(e)
        return e


    def add_node(self,index=None):
        n = Node(index)
        self.nodes.append(n)
        return n

    def remove_edge(self,edge):
        self.edges.remove(edge)
        del edge

    def remove_node(self,node):
        self.nodes.remove(node)
        del node

    def max_weight(self,departure,arrival):
        if departure not in self.nodes or arrival not in self.nodes:
            return -1
        self.max_weight_return_list=[]
        self.__pathing_list(departure,arrival)
        shortest_path=-1
        for path in self.max_weight_return_list:
            path_weight=0
            for edge in path:
                path_weight = path_weight+edge.weight
            if path_weight < shortest_path or shortest_path == -1:
                shortest_path = path_weight
        del self.max_weight_return_list

    # percorrer partida até chegada, procurando o menor caminho
    def min_weight(self,departure,arrival):
        if departure not in self.nodes or arrival not in self.nodes:
            return -1
        self.min_weight_return_list=[]
        self.__pathing_list(departure,arrival)
        shortest_path=-1
        for path in self.min_weight_return_list:
            path_weight=0
            for edge in path:
                path_weight = path_weight+edge.weight
            if path_weight < shortest_path or shortest_path == -1:
                shortest_path = path_weight
        del self.min_weight_return_list


    def most_connected(self):
        conn_number = -1
        r_node = None
        for node in self.nodes:
            if len(node.edges) > conn_number:
                r_node = node
                conn_number=len(node.edges)
        return r_node

    def least_connected(self):
        conn_number = -1
        r_node = None
        for node in self.nodes:
            if len(node.edges) < conn_number:
                r_node = node
                conn_number=len(node.edges)
        return r_node



    '''
========================================================
========================================================
========================================================
    '''
    
    def __pathing_list(self,current,arrival,edge_list=[]):
        for edge in current.edges:
            if edge not in edge_list:
                edge_list.append(edge)
                lookup = edge.next(current)
                if lookup == arrival:
                    self.min_weight_return_list.append(edge_list)
                    break
                else:
                    self.__pathing_list(lookup,arrival,edge_list)

    def print(self):
        for node in self.nodes:
            print("Node",node.name,"\n    ",end="")
            for edge in node.edges:
                print(edge.name," ",end="")
            print("")


    def __del__(self):
        for node in self.nodes:
            del node
        print("Graph Deleted!")