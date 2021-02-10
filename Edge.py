
class Edge:
    index=0
    def __init__(self,graph,weight=1,name=None,direc=None):
        self.owner=graph
        self.id=Edge.index
        Edge.index=Edge.index+1
        
        if name:
            self.name = name
        else:
            self.name='e'+str(self.id)

        self.weight=weight
        self.direc=False if not direc else direc
    
    def copy(self):
        return Edge(self.owner,self.weight,self.name,self.direc)

    def __del__(self):
        self.owner.remove_edge(self)
        #print("Edge",self.name,"deleted!")