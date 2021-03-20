# noinspection SpellCheckingInspection
class Edge:
    index = 0

    def __init__(self, graph, weight=1, name=None, direc=None):
        self.owner = graph
        self.id = Edge.index
        self.__capacidade = None
        self.__fluxo = None
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

    def get_fluxo(self): return self.__fluxo
    def get_capacidade(self):return self.__capacidade

    def __repr__(self):
        return self.name