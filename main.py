from Graph import Graph

def print_arvore(gs):
    if gs.arvore(gs.ciclos()) == True:
        print("ARVORE\n")
    else:
        print("NAO É ARVORE\n")

g1 = Graph("Questao 1-conexo-ciclico")
n1=g1.add_node()
n2=g1.add_node()
n3=g1.add_node()
n4=g1.add_node()

g1.add_edge(n1,n2)
g1.add_edge(n1,n3)
g1.add_edge(n3,n2)
g1.add_edge(n1,n4)
g1.add_edge(n3,n4)

g2 = Graph("Questao 1-conexo-aciclico")
n1=g2.add_node()
n2=g2.add_node()
n3=g2.add_node()
n4=g2.add_node()
n5=g2.add_node()
n6=g2.add_node()

g2.add_edge(n1,n2)
g2.add_edge(n1,n3)
g2.add_edge(n2,n4)
g2.add_edge(n2,n5)
g2.add_edge(n3,n6)

# Passei por aqui

g3 = Graph("Questao 1-desconexo")
n1=g3.add_node()
n2=g3.add_node()
n3=g3.add_node()
n4=g3.add_node()

g3.add_edge(n1,n2)
g3.add_edge(n3,n4)

print_arvore(g1)
print_arvore(g2)
print_arvore(g3)


g4 = Graph("Questao 2-conexo-1-ponte")

g5 = Graph("Questao 2-conexo-+1-ponte")