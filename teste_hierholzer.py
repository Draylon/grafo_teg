
from Graph import Graph, isomorfo


cruzamentos = 5 # número de cruzamentos colocados
grafo = Graph("asd",direcionado=True) # Direcionado
cl = [ grafo.add_node("c"+str(i)) for i in range(cruzamentos)]

grafo.add_edge(cl[0],cl[1])
grafo.add_edge(cl[1],cl[2])
grafo.add_edge(cl[1],cl[3])
grafo.add_edge(cl[2],cl[0])
grafo.add_edge(cl[3],cl[4])
grafo.add_edge(cl[4],cl[1])

#print(grafo.ciclos())

grafo.verifica_euleriano()
print(grafo.hierholzer())
print(grafo.hierholzer2())