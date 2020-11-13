
class Node:
    node_counter=0
    def __init__(self,name=None):
        self.edges=[]
        self.index=Node.node_counter
        Node.node_counter=Node.node_counter+1
        if name:
            self.name=name
        else:
            self.index=str(node_counter)

    def add_edge(self,edge):
        self.edges.append(edge)
    def remove_edge(self,edge):
        return self.edges.remove(edge)

    def next(self,edge):
        return edge.next(self)
    

    def __del__(self):
        for edge in self.edges:
            del edge
        Node.node_counter=Node.node_counter-1
        print("Node deleted!")