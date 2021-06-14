from Graph import *
from networkx_adapter import *

grafo = Graph("asd",True) # Direcionado
grafo2 = Graph("sub-asd",True) # Direcionado

cruzamentos = 6 # número de cruzamentos colocados
cl = [ grafo.add_node("c"+str(i)) for i in range(cruzamentos)]
for i in cl[2:5]: grafo2.add_node_object(i)

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

#grafo2.add_node("c6")
grafo2.add_edge(cl[2],cl[4])


print( grafo2.get_edges())
print( grafo.get_edges())
print(all(elem in grafo.get_edges() for elem in grafo2.get_edges()))


#print(sub_grafo(grafo,grafo2))

#grafo.print_dfs(grafo.dfs(cl[0]))

"""
pos = {0:(2,3),1:(4,2),2:(0,2),3:(3,0),4:(1,0),5:(2,1)}
nxg = create_networkx_graph(grafo)
#networkx_draw(nxg,grafo.get_node_connections())
networkx_draw(nxg,grafo.get_node_connections(),pos,True)
"""