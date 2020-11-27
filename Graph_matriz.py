
from Node import Vertice
#from Edge import Edge

class Graph:
    def complemento(grafo):
        matr=[ [ (0 if grafo.matrizAdjacencias[x][y] == 1 else 1) for y in range(len(grafo.matrizAdjacencias[0]))]  for x in range(len(grafo.matrizAdjacencias)) ]
        grp=Graph()
        grp.matrizAdjacencias=matr
        grp.listaVertices=grafo.listaVertices
        grp.numVerticesMaximo=grafo.numVerticesMaximo
        grp.numVertices=grafo.numVertices
        return grp
    def conexo(grafo):
        for xi,x in enumerate(grafo.matrizAdjacencias):
            sum=0
            for yi,y in enumerate(grafo.matrizAdjacencias[xi]):
                sum+=y


    def __init__(self,name=None,direcionado=False):
        self.numVerticesMaximo=3
        self.numVertices = 0
        self.listaVertices = []
        self.matrizAdjacencias = [ [0 for y in range(self.numVerticesMaximo)] for x in range(self.numVerticesMaximo)]

    def add_edge(self,inicio,fim):
        inicio=self.getIndex(inicio)
        fim=self.getIndex(fim)
        self.matrizAdjacencias[inicio][fim] += 1
        self.matrizAdjacencias[fim][inicio] += 1

    def add_node(self,name=None):
        self.numVertices += 1
        self.listaVertices.append(Vertice(name))
        return self.listaVertices[self.numVertices-1]

    def remove_edge(self,edge):
        inicio=self.getIndex(inicio)
        fim=self.getIndex(fim)
        self.matrizAdjacencias[inicio][fim]-=1
        self.matrizAdjacencias[fim][inicio]-=1

    def remove_node(self,node):
        self.numVertices -= 1
        self.listaVertices.remove(node)
        del node

    def getIndex(self,node):
        return self.listaVertices.index(node)

    def grau(self,node):
        ind = self.getIndex(node)
        g=0
        if not self.matrizAdjacencias[ind]: return g
        for xi,x in enumerate(self.matrizAdjacencias[ind]):
            g+= x*2 if ind==xi else x
        return g
    
    



    def most_connected(self):
        most_ = []
        ammo,xn = -1,0
        for xi,x in enumerate(self.matrizAdjacencias):
            new_ammo=0
            for yi,y in enumerate(x):
                new_ammo+= 2*y if xi==yi else y
            if new_ammo == ammo:
                most_.append(xn)
            if new_ammo > ammo or ammo==-1:
                most_=[xn]
                ammo=new_ammo

            xn+=1
        return most_,ammo

    def least_connected(self):
        most_ = []
        ammo,xn = -1,0
        for xi,x in enumerate(self.matrizAdjacencias):
            new_ammo=0
            for yi,y in enumerate(x):
                new_ammo+= 2*y if xi==yi else y
            if new_ammo == ammo:
                most_.append(xn)
            if new_ammo < ammo or ammo==-1:
                most_=[xn]
                ammo=new_ammo

            xn+=1
        return most_,ammo


    
    def print_matriz(self):
        for x in self.matrizAdjacencias:
            for y in x:
                print(y,end=" ")
            print("")


    def __del__(self):
        for node in self.listaVertices:
            del node
        print("Graph Deleted!")