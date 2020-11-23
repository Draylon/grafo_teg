
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

    def __init__(self,name=None,direcionado=False):
        self.numVerticesMaximo=3
        self.numVertices = 0
        self.listaVertices = []
        self.matrizAdjacencias = [ [0 for y in range(self.numVerticesMaximo)] for x in range(self.numVerticesMaximo)]

    def add_edge(self,inicio,fim):
        self.matrizAdjacencias[inicio][fim] = 1
        self.matrizAdjacencias[fim][inicio] = 1

    def add_node(self,name=None):
        self.numVertices += 1
        self.listaVertices.append(Vertice(name))
        return self.numVertices-1

    def remove_edge(self,edge):
        self.matrizAdjacencias[inicio][fim] =0
        self.matrizAdjacencias[fim][inicio] =0

    def remove_node(self,node):
        self.numVertices -= 1
        self.listaVertices.remove(node)
        return self.numVertices

    def localizaRotulo(self,rinicio):
        return self.listaVertices[rinicio]


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