
class Node:
    node_counter=0
    def __init__(self,name=None):
        self.edges=[]
        self.index=Node.node_counter
        Node.node_counter=Node.node_counter+1
        if(name)
            self.name=name
        else:
            self.index=str(node_counter)
    
    def add_edge(self,edge):
        self.edges.append(edge)

    def remove_edge(self,edge):
        return self.edges.remove(edge)

    def __del__(self):
        Node.node_counter=Node.node_counter-1