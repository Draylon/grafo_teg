
from Graph import Graph, isomorfo


cruzamentos = 4 # número de cruzamentos colocados
grafo = Graph("asd") # Direcionado
cl = [ grafo.add_node("c"+str(i+1)) for i in range(cruzamentos)]

grafo.add_edge(cl[0],cl[1],10)
grafo.add_edge(cl[0],cl[2],15)
grafo.add_edge(cl[0],cl[3],20)
grafo.add_edge(cl[1],cl[2],35)
grafo.add_edge(cl[1],cl[3],25)
grafo.add_edge(cl[2],cl[3],30)

#print(grafo.ciclos())

#print(grafo.bfs_tree(cl[0]))
print(grafo.travelling_salesman2(cl[0]))