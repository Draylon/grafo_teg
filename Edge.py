
class Edge:
    edge_counter=0
    def __init__(self,name=None,weight=1,node1,node2,direc=None):
        self.index=Edge.edge_counter
        Edge.edge_counter=Edge.edge_counter+1
        
        if(name)
            self.name = name
        else:
            self.name=self.index

        self.weight=weight
        self.nodes=[node1,node2]
        self.direc=direc

    ''' pega o nodo na outra ponta'''
    def next(self,node=None):
        if self.direc == True:
            return self.nodes[1]

        if self.nodes[0] == node:
            return self.nodes[0]
        elif self.nodes[1] == node:
            return self.nodes[1]
        else
            return None

    
    def __del__(self):
        for node in self.nodes:
            node.remove_edge(self)
        Edge.edge_counter=Edge.edge_counter-1