from Graph import Graph, isomorfo

#Seja G=(V,E) um grafo não-direcionado onde V={'A','B','C','D'} e E={(A,C),(A,D),(B,C),(B,D)}. Assinale a alternativa correta:

"""
cruzamentos = 5 # número de cruzamentos colocados
grafo = Graph("asd") # Direcionado
grafo2 = Graph("asd") # Direcionado
#cl1 = [ grafo.add_node("c"+str(i)) for i in range(cruzamentos)]
cla = grafo.add_node("A")
clb = grafo.add_node("B")
clc = grafo.add_node("C")
cld = grafo.add_node("D")

grafo2.add_node_object(cla)
grafo2.add_node_object(clb)
grafo2.add_node_object(clc)
grafo2.add_node_object(cld)

grafo.add_edge(cla,clc)
grafo.add_edge(cla,cld)
grafo.add_edge(clb,clc)
grafo.add_edge(clb,cld)

print(grafo.conexo())
print("")
print(grafo.planar(grafo.list_grau_conexoes()))
print("")
print(grafo.bipartido(cla))
print(grafo.bipartido(clb))
print(grafo.bipartido(clc))
print(grafo.bipartido(cld))
print("")
print(grafo.bipartido2())

"""

#um teste com Elis e Pedro deveria retornar verdadeiro (existe parentesco) e entre Zec e Perf deveria retornar falso

grafo = Graph("vacas",direcionado=True)
juca = grafo.add_node("juca")
caju = grafo.add_node("caju")
alice = grafo.add_node("alice")
bob = grafo.add_node("bob")
marie = grafo.add_node("marie")
olivier = grafo.add_node("olivier")
gin = grafo.add_node("gin")
gina = grafo.add_node("gina")
bonnie = grafo.add_node("bonnie")
perf = grafo.add_node("perf")
zec = grafo.add_node("zec")
pedro = grafo.add_node("pedro")
elis = grafo.add_node("elis")


grafo.add_edge(juca,olivier)
grafo.add_edge(juca,gin)
grafo.add_edge(caju,olivier)
grafo.add_edge(caju,gin)
grafo.add_edge(alice,gina)
grafo.add_edge(alice,bonnie)
grafo.add_edge(bob,gina)
grafo.add_edge(bob,bonnie)
grafo.add_edge(marie,zec)
grafo.add_edge(olivier,zec)
grafo.add_edge(gin,pedro)
grafo.add_edge(gina,pedro)
grafo.add_edge(bonnie,elis)
grafo.add_edge(perf,elis)

print(grafo.find_common_parents(zec,perf))
print(grafo.find_common_parents(zec,pedro))
print(grafo.find_common_parents(elis,pedro))


'''dfs(graph G, vertex s, vertex d):
    for v in G.vertex:

        v.explored = 0
    Stack P;
    P.push(s);

    while(P.size != 0):
        v = P.pop();

        if v == d: # parar no destino

            return true

        v.explored = true; 

        for u in G.neighbor[v]:  # nodes vizinhos de V

            if u.explored == 0:

                P.push(u)'''