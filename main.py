from Graph import Graph

'''

    Alunos: Draylon Lopes e Victor Bernardes

'''


grafo = Graph("Questao 1",True)
s = grafo.add_node("S")
v1 = grafo.add_node("V1")
v2 = grafo.add_node("V2")
v3 = grafo.add_node("V3")
v4 = grafo.add_node("V4")
v5 = grafo.add_node("V5")
t = grafo.add_node("T")

grafo.add_edge(s, v1,'8/8',8,8)

grafo.add_edge(s, v2,'5/4',5,4)
grafo.add_edge(v1, v2,'10/2',10,2)

grafo.add_edge(s, v3,'10/3',10,3)
grafo.add_edge(v1, v3,'3/3',3,3)

grafo.add_edge(v1, v4,'5/3',5,3)
grafo.add_edge(v2, v4,'3/0',3,0)
grafo.add_edge(v3, v4,'5/3',5,3)

grafo.add_edge(v2, v5,'6/5',6,5)
grafo.add_edge(v3, v5,'3/0',3,0)
grafo.add_edge(v4, v5,'8/6',8,6)

grafo.add_edge(v2, t,'5/1',5,1)
grafo.add_edge(v3, t,'4/3',4,3)
grafo.add_edge(v5, t,'12/11',12,11)


lst = grafo.dfs(s)
for node,index in lst.items():
    print(node," tem profundidade ",index)

lst2 = grafo.dfs_paths(s,t)
'''edges = grafo.fluxo(s,t,1)
for edge in edges:
    print(edge)'''



flow = grafo.edmondsKarp(s,t)
print("Edmonds Karp",flow)

print("Ford Fulkerson",grafo.ford_fulkerson(s,t))

grafo.print_matriz('capacidade')
grafo.print_matriz('fluxo')