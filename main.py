from Graph import Graph

def print_arvore(gs):
    if gs.arvore(gs.ciclos()) == True:
        print("ARVORE\n")
    else:
        print("NAO É ARVORE\n")

#=================================================
#=================================================

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


g3 = Graph("Questao 1-desconexo")
n1=g3.add_node()
n2=g3.add_node()
n3=g3.add_node()
n4=g3.add_node()

g3.add_edge(n1,n2)
g3.add_edge(n3,n4)

#print_arvore(g1)
#print_arvore(g2)
#print_arvore(g3)

#=================================================
#=================================================

g4 = Graph("Questao 2-conexo-1-ponte")

n1=g4.add_node()
n2=g4.add_node()
n3=g4.add_node()
n4=g4.add_node()
n5=g4.add_node()
n6=g4.add_node()

g4.add_edge(n1,n2)
g4.add_edge(n1,n3)
g4.add_edge(n2,n3)
g4.add_edge(n4,n5)
g4.add_edge(n4,n6)
g4.add_edge(n5,n6)
g4.add_edge(n1,n4,"Stonks")

#Graph.print_pontes(g4.pontes(g4.ciclos()))


#=================================================
#=================================================


g5 = Graph("Questao 2-conexo-+1-ponte")

n1=g5.add_node()
n2=g5.add_node()
n3=g5.add_node()
n4=g5.add_node()
n5=g5.add_node()
n6=g5.add_node()
n7=g5.add_node()
n8=g5.add_node()
n9=g5.add_node()
n10=g5.add_node()
n11=g5.add_node()
n12=g5.add_node()

g5.add_edge(n1,n2)
g5.add_edge(n1,n3)
g5.add_edge(n2,n3)

g5.add_edge(n4,n5)
g5.add_edge(n4,n6)
g5.add_edge(n5,n6)

g5.add_edge(n7,n8)
g5.add_edge(n7,n9)
g5.add_edge(n8,n9)

g5.add_edge(n10,n11)
g5.add_edge(n10,n12)
g5.add_edge(n11,n12)

g5.add_edge(n1,n4,"Stonks")
g5.add_edge(n1,n7,"Stonks2")

g5.add_edge(n1,n10,"Stonks3")

#Graph.print_pontes(g5.pontes(g5.ciclos()))


#=================================================
#=================================================

def similar(n1,n2):
    if len(n1) != len(n2):
        return False
    lenc=len(n1)
    iic=0
    caracter_diferente=False
    while iic < lenc:
        if n1[iic] != n2[iic]:
            if caracter_diferente:
                return False
            caracter_diferente=True
        iic+=1
    return True


lista_nodes = []
lista_palavras = ['caiado', 'cavado', 'cavalo', 'girafa', 'girava', 'ralo', 'ramo', 'rata', 'rato', 'remo', 'reta', 'reto', 'rota', 'vaiado', 'varado', 'virada', 'virado', 'virava', 'rita', 'cavala', 'cabala']
#lista_palavras = ['caiado', 'cavado', 'cavalo', 'girafa', 'girava']
del_count=0

node_selecionado=None
g6 = Graph("Questao 3")

for palavra in lista_palavras:
    lista_nodes.append(g6.add_node(palavra))

node_len = len(lista_nodes)

while len(lista_palavras) > 0:
    node_i = del_count
    while node_i < node_len:
        if node_selecionado==None:
            node_selecionado=lista_nodes[node_i]
            lista_palavras.remove(node_selecionado.name)
            del_count+=1
        else:
            if (similar(lista_nodes[node_i].name,node_selecionado.name)) == True:
                g6.add_edge(node_selecionado,lista_nodes[node_i])
        node_i+=1
    node_selecionado=None


g6.print()
lista_subgrafos = g6.sub_grafos()
g6.print_subgrafos(lista_subgrafos)