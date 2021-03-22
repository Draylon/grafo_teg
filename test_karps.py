from Graph import Graph
from networkx_adapter import *

'''

    Alunos: Draylon Lopes e Victor Bernardes

'''


grafo = Graph("Questao 1",True)
#pos = {0: (0, 1), 1: (1, 1), 2: (2,0), 3: (2, 2),4:(3,1),5:(4,1),6:(5,1)}
s = grafo.add_node("S",position=(0,1))
v1 = grafo.add_node("V1",position=(1,1))
v2 = grafo.add_node("V2",position=(2,0))
v3 = grafo.add_node("V3",position=(2,2))
v4 = grafo.add_node("V4",position=(3,1))
v5 = grafo.add_node("V5",position=(4,1))
t = grafo.add_node("T",position=(5,1))

grafo.add_edge(s, v1,'8/8',8,0)

grafo.add_edge(s, v2,'5/4',5,0)
grafo.add_edge(v1, v2,'10/2',10,0)

grafo.add_edge(s, v3,'10/3',10,0)
grafo.add_edge(v1, v3,'3/3',3,0)

grafo.add_edge(v1, v4,'5/3',5,0)
grafo.add_edge(v2, v4,'3/0',3,0)
grafo.add_edge(v3, v4,'5/3',5,0)

grafo.add_edge(v2, v5,'6/5',6,0)
grafo.add_edge(v3, v5,'3/0',3,0)
grafo.add_edge(v4, v5,'8/6',8,0)

grafo.add_edge(v2, t,'5/1',5,0)
grafo.add_edge(v3, t,'4/3',4,0)
grafo.add_edge(v5, t,'12/11',12,0)


lst = grafo.dfs(s)
for node,index in lst.items():
    print(node," tem profundidade ",index)

lst2 = grafo.dfs_paths(s,t)

print("Edmonds Karp",grafo.edmondsKarp(s,t))


grafo.print_matriz('capacidade')
grafo.print_matriz('fluxo')

nxg = create_networkx_graph(grafo)
networkx_draw(nxg,grafo.get_node_connections())