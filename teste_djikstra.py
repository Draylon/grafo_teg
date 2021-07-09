from Graph import Graph

grafo = Graph("asd",True) # Direcionado
a = grafo.add_node("A")
b = grafo.add_node("B")
c = grafo.add_node("C")
d = grafo.add_node("D")
e = grafo.add_node("E")

grafo.add_edge(a,b,weight=-1)
grafo.add_edge(a,c,weight=4)
grafo.add_edge(b,e,weight=2)
grafo.add_edge(b,d,weight=2)
grafo.add_edge(b,c,weight=3)
grafo.add_edge(d,b,weight=1)
grafo.add_edge(e,d,weight=-3)

grafo.dijkstra(a)