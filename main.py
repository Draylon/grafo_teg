from Graph import Graph

'''

    Alunos: Draylon Lopes e Victor Bernardes

'''

grafo = Graph("DIGRAFO",True)
s = grafo.add_node("S")
v1 = grafo.add_node("v1")
v2 = grafo.add_node("v2")
v3 = grafo.add_node("v3")
v4 = grafo.add_node("v4")
v5 = grafo.add_node("v5")
t = grafo.add_node("T")

grafo.add_edge(s, v1)
grafo.add_edge(s, v2)
grafo.add_edge(s, v3)

grafo.add_edge(v1, v2)
grafo.add_edge(v1, v3)
grafo.add_edge(v1, v4)
grafo.add_edge(v2, v4)
grafo.add_edge(v3, v4)

grafo.add_edge(v2, v5)
grafo.add_edge(v3, v5)
grafo.add_edge(v4, v5)

grafo.add_edge(v2, t)
grafo.add_edge(v3, t)
grafo.add_edge(v5, t)

lst = grafo.dfs(s)
for node,index in lst.items():
    print(node," tem profundidade ",index)