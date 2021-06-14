# noinspection SpellCheckingInspection
class Edge:
    index = 0

    def __init__(self, graph, weight=1, name=None, direc=None,capacidade=0,fluxo=0,parallel=False):
        self.owner = graph
        self.id = Edge.index
        self.__capacidade = capacidade
        self.__fluxo = fluxo
        self.parallel=parallel
        Edge.index = Edge.index + 1

        if name:
            self.name = name
        else:
            self.name = 'e' + str(self.id)

        self.weight = weight
        self.direc = False if not direc else direc

    def copy(self):
        return Edge(self.owner, self.weight, self.name, self.direc)

    def __del__(self):
        self.owner.remove_edge(self)
        # print("Edge",self.name,"deleted!")

    def set_fluxo(self, capacidade, fluxo):
        self.__capacidade = capacidade
        self.__fluxo = fluxo

    def addCap(self,val):
        self.__capacidade+=val
        self.setName()
    def addFlux(self,val):
        self.__fluxo+=val
        self.setName()

    def setCap(self,val):
        self.__capacidade=val
        self.setName()
    def setFlux(self,val):
        self.__fluxo=val
        self.setName()


    def getFlux(self): return self.__fluxo
    def getCap(self):return self.__capacidade
    def capacidade(self):return self.__capacidade

    def setName(self):
        self.name = str(self.__capacidade) + "/" + str(self.__fluxo)
        #self.name = str(self.__fluxo)

    def __repr__(self):
        return self.name

    def __eq__(self, value):
        if type(value) == Edge:
            if self.name == value.name and self.weight == value.weight:
                return True
        return False

    def __hash__(self):
        return self.id