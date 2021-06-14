from Graph import Graph

grafo = Graph("asd") # Direcionado

cruzamentos = 6 # número de cruzamentos colocados
cl = [ grafo.add_node("c"+str(i)) for i in range(cruzamentos)]

grafo.add_edge(cl[0],cl[1])
grafo.add_edge(cl[0],cl[2])
grafo.add_edge(cl[1],cl[3])
grafo.add_edge(cl[3],cl[0])
grafo.add_edge(cl[2],cl[1])
grafo.add_edge(cl[5],cl[3])
grafo.add_edge(cl[4],cl[5])
grafo.add_edge(cl[4],cl[0])
grafo.add_edge(cl[1],cl[4])
grafo.add_edge(cl[2],cl[4])

#print("coloracao:",grafo.coloracao())
#print("bipartido:",grafo.bipartido2())
print(grafo.list_grau_conexoes())

"""
print("completo: ",grafo.completo())
print("adjacente:",grafo.adjacente(cl[0],cl[1]))
print("Edges que levam de",cl[0],"até",cl[3])
print(grafo.dfs_paths(cl[0],cl[3]))
"""