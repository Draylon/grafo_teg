from Graph import Graph, isomorfo


cruzamentos = 5 # número de cruzamentos colocados
grafo = Graph("asd") # Direcionado
cl = [ grafo.add_node("c"+str(i)) for i in range(cruzamentos)]

grafo.add_edge(cl[0],cl[1])
grafo.add_edge(cl[0],cl[2])
grafo.add_edge(cl[0],cl[3])
grafo.add_edge(cl[0],cl[4])
grafo.add_edge(cl[1],cl[2])
grafo.add_edge(cl[1],cl[3])
grafo.add_edge(cl[1],cl[4])
grafo.add_edge(cl[2],cl[3])
grafo.add_edge(cl[2],cl[4])
grafo.add_edge(cl[3],cl[4])

print(grafo.completo())
a = grafo.planar(grafo.list_grau_conexoes())
print(a)