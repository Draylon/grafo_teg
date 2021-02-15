
class Node:
    index=0
    def __init__(self,graph,name=None):
        self.owner=graph
        self.id=Node.index
        self.name=""

        if name: self.name=name
        else: self.name='n'+str(self.id)
        
        Node.index=Node.index+1
    
    def copy(self):
        return Node(self.owner,self.name)

    def __del__(self):
        self.owner.remove_node(self)
        #print("Node",self.name,"deleted!")
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