
from Graph import Graph


cruzamentos = 4 # número de cruzamentos colocados
grafo = Graph("asd")
cl = [ grafo.add_node("c"+str(i+1)) for i in range(cruzamentos)]

grafo.add_edge(cl[0],cl[1],10)
grafo.add_edge(cl[0],cl[2],10)
grafo.add_edge(cl[1],cl[2],15)
grafo.add_edge(cl[1],cl[3],20)

subg = grafo.sub_grafos()
ciclos = grafo.ciclos()

print("conexo:",grafo.conexo(subg))
print("subgrafo:",subg)
print("ciclos:",ciclos)
print("arvore:",grafo.arvore(ciclos,subg))
kr = grafo.kruskal()
print("arvore geradora minima: ",kr.get_edges())
subg2=kr.sub_grafos()
ciclos2=kr.ciclos()
print("é arvore?:",kr.arvore(ciclos2,subg2))
