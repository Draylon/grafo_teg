from Graph import Graph, isomorfo


cruzamentos = 9 # número de cruzamentos colocados
grafo = Graph("asd") # Direcionado
cl = [ grafo.add_node("c"+str(i)) for i in range(cruzamentos)]

#k3,3
"""
grafo.add_edge(cl[0],cl[3])
grafo.add_edge(cl[0],cl[4])
grafo.add_edge(cl[0],cl[5])

grafo.add_edge(cl[1],cl[3])
grafo.add_edge(cl[1],cl[4])
grafo.add_edge(cl[1],cl[5])

grafo.add_edge(cl[2],cl[3])
grafo.add_edge(cl[2],cl[4])
grafo.add_edge(cl[2],cl[5])
"""

#k3,3

"""grafo.add_edge(cl[0],cl[1])
grafo.add_edge(cl[0],cl[3])
grafo.add_edge(cl[0],cl[5])

grafo.add_edge(cl[2],cl[1])
grafo.add_edge(cl[2],cl[3])
grafo.add_edge(cl[2],cl[5])

grafo.add_edge(cl[4],cl[1])
grafo.add_edge(cl[4],cl[3])
grafo.add_edge(cl[4],cl[5])"""


#k5
"""grafo.add_edge(cl[0],cl[1])
grafo.add_edge(cl[0],cl[2])
grafo.add_edge(cl[0],cl[3])
grafo.add_edge(cl[0],cl[4])

grafo.add_edge(cl[1],cl[2])
grafo.add_edge(cl[1],cl[3])
grafo.add_edge(cl[1],cl[4])

grafo.add_edge(cl[2],cl[3])
grafo.add_edge(cl[2],cl[4])

grafo.add_edge(cl[3],cl[4])"""

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


#triangulo
"""grafo.add_edge(cl[0],cl[1])
grafo.add_edge(cl[0],cl[2])
grafo.add_edge(cl[1],cl[2])"""

#grafo.bfs_print(cl[0])
#print("coloracao:",grafo.coloracao())
#print("bipartido:",grafo.bipartido2())
#print("Planar: ",grafo.planar())
#print("Ciclos")
grafo.ciclos()
#print(isomorfo(grafo,grafo))
"""
{
    4:[ [2,2,3,5], 3 ],
    2:[ [1,3],1 ]
}
"""
