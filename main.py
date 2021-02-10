from Graph import Graph

g = Graph("Questao 1-conexo-ciclico")
n1=g.add_node()
n2=g.add_node()
n3=g.add_node()
n4=g.add_node()

e1=g.add_edge(n1,n2)
e2=g.add_edge(n1,n3)
e3=g.add_edge(n3,n2)
e4=g.add_edge(n1,n4)
e5=g.add_edge(n3,n4)

gconexo=g.conexo()
gciclico=Graph.ciclico(g.ciclos())

if(gconexo and gciclico):
    print("ARVORE")
else:
    print("NAO É ARVORE")


g = Graph("Questao 1-conexo-aciclico")
n1=g.add_node()
n2=g.add_node()
n3=g.add_node()
n4=g.add_node()
n5=g.add_node()
n6=g.add_node()

e1=g.add_edge(n1,n2)
e2=g.add_edge(n1,n3)
e3=g.add_edge(n2,n4)
e4=g.add_edge(n2,n5)
e5=g.add_edge(n3,n6)

gconexo=g.conexo()
gciclico=Graph.ciclico(g.ciclos())

if(gconexo and gciclico):
    print("ARVORE")
else:
    print("NAO É ARVORE")


g = Graph("Questao 1-desconexo")
n1=g.add_node()
n2=g.add_node()
n3=g.add_node()
n4=g.add_node()

e1=g.add_edge(n1,n2)
e2=g.add_edge(n3,n4)

gconexo=g.conexo()
gciclico=Graph.ciclico(g.ciclos())

if(gconexo and gciclico):
    print("ARVORE")
else:
    print("NAO É ARVORE")