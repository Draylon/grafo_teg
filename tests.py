from Graph import Graph

'''

    Alunos: Draylon Lopes e Victor Bernardes

'''


'''grafo = Graph("Questao 1",True)
s = grafo.add_node("S")
v1 = grafo.add_node("V1")
v2 = grafo.add_node("V2")
v3 = grafo.add_node("V3")
v4 = grafo.add_node("V4")
v5 = grafo.add_node("V5")
t = grafo.add_node("T")

grafo.add_edge(s, v1,'8/8',8,8)

grafo.add_edge(s, v2,'5/4',5,4)
grafo.add_edge(v1, v2,'10/2',5,4)

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
edges = grafo.fluxo(s,t,1)
for edge in edges:
    print(edge)'''


'''grafo = Graph("FLUXO MAXIMO TESTE",True)
g0 = grafo.add_node('0')
g1 = grafo.add_node('1')
g2 = grafo.add_node('2')
g3 = grafo.add_node('3')

grafo.add_edge(g0,g1,capacidade=1000000)
grafo.add_edge(g0,g2,capacidade=1000000)

grafo.add_edge(g1,g2,capacidade=1)
grafo.add_edge(g1,g3,capacidade=1000000)

grafo.add_edge(g2,g3,capacidade=1000000)

flow = grafo.edmondsKarp(g0,g3)

print(flow)
'''

grafo = Graph("Teste Fulkerson",True)
g0 = grafo.add_node('0')
g1 = grafo.add_node('1')
g2 = grafo.add_node('2')
g3 = grafo.add_node('3')
g4 = grafo.add_node('4')
g5 = grafo.add_node('5')

grafo.add_edge(g0,g1,capacidade=8)
grafo.add_edge(g0,g4,capacidade=3)

grafo.add_edge(g1,g2,capacidade=9)
grafo.add_edge(g1,g0,capacidade=0)


grafo.add_edge(g2,g4,capacidade=7)
grafo.add_edge(g2,g1,capacidade=0)
grafo.add_edge(g2,g5,capacidade=2)


grafo.add_edge(g3,g5,capacidade=5)
grafo.add_edge(g3,g4,capacidade=0)

grafo.add_edge(g4,g2,capacidade=7)
grafo.add_edge(g4,g3,capacidade=4)
grafo.add_edge(g4,g0,capacidade=0)

grafo.add_edge(g5,g2,capacidade=0)
grafo.add_edge(g5,g3,capacidade=0)

print("Max Flow: %d " % grafo.ford_fulkerson(g0,g5))