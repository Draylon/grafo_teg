
class Edge:
    edge_counter=0
    def __init__(self,name=None,weight=1,node1,node2):
        self.index=Edge.edge_counter
        Edge.edge_counter=Edge.edge_counter+1
        if(name)
            self.name = name
        else:
            self.name=self.index
        self.weight=weight
        self.nodes=[node1,node2]

    def next(self,node):
        if(self.nodes[0] == node)
            return self.nodes[0]
        else:
            return self.nodes[1]