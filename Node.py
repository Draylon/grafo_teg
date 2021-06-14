
class Node:
    index=0
    def __init__(self,graph,name=None,position=()):
        self.position=position
        self.owner=graph
        self.id=Node.index
        self.name=""

        if name: self.name=name
        else: self.name='n'+str(self.id)
        
        Node.index+=1
    
    def copy(self):
        return Node(self.owner,self.name)

    def __index__(self):
        return self.id

    def __del__(self):
        self.owner.remove_node(self)
        #Node.index-=1
        #print("Node",self.name,"deleted!")

    def __repr__(self):
        return self.name

    def __eq__(self, value):
        if type(value) != Node:
            return False
        if self.name == value.name:
            return True
        return False
    
    def __hash__(self):
        return self.id
'''
class Vertice:
    index=0
    def __init__(self,rotulo):
        self.id=Vertice.index
        self.rotulo = rotulo # por exemplo "A"
        self.visitado = False
        Vertice.index+=1
    # def visitado(self):
    #        self.visitado = True
    def igualA(self,r):
        return r == self.rotulo
    def foiVisitado(self):
        return self.visitado
    def regVisitado(self):
        self.visitado = True
    def limpa(self):
        self.visitado = False
    
    def __del__(self):
        Vertice.index-=1
        '''