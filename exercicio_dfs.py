from Graph import Graph, isomorfo


cruzamentos = 9 # número de cruzamentos colocados
grafo = Graph("grafo")
cl = [ grafo.add_node("c"+str(i)) for i in range(cruzamentos)]

grafo.add_edge(cl[0],cl[1])
grafo.add_edge(cl[0],cl[3])
grafo.add_edge(cl[0],cl[4])
grafo.add_edge(cl[0],cl[5])
grafo.add_edge(cl[1],cl[2])
#grafo.add_edge(cl[1],cl[3])
grafo.add_edge(cl[2],cl[3])
grafo.add_edge(cl[2],cl[7])
#grafo.add_edge(cl[3],cl[4])
grafo.add_edge(cl[3],cl[7])
grafo.add_edge(cl[4],cl[5])
grafo.add_edge(cl[4],cl[6])
grafo.add_edge(cl[5],cl[6])
#grafo.add_edge(cl[6],cl[7])
grafo.add_edge(cl[6],cl[8])
grafo.add_edge(cl[7],cl[8])

print(grafo.dfs_print(cl[0]))