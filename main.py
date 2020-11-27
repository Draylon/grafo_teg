
from Graph import Graph

if __name__ == "__main__":

    print("\n\n========================\n========================\n\n       Caso1:     \n\n========================\n========================\n\n")

    graph=Graph()
    n1=graph.add_node('a1')
    n2=graph.add_node('a2')
    n3=graph.add_node('a3')
    e1=graph.add_edge(n1,n1)
    e2=graph.add_edge(n1,n2)
    e3=graph.add_edge(n1,n3)
    e4=graph.add_edge(n2,n3)

    #graph.remove_edge(e1)

    graph.print()
    graph.print_matriz()
    print("Menos conectado:")
    ar,ammo = graph.least_connected()
    print(ar,end=" ")
    print("com grau",ammo,"\n")
    print("Mais conectado:")
    ar,ammo = graph.most_connected()
    print(ar,end=" ")
    print("com grau",ammo,"\n")
    
    graph.grau_vertices()

    print("subgs:\n")
    sg1=graph.sub_grafos()
    graph.print_subgrafos(sg1)
    gc,gcm = graph.conexo()
    


    print("\n\n========================\n========================\n\n       Caso2:     \n\n========================\n========================\n\n")
    
    g2=Graph.complemento(graph)
    g2.print()
    g2.print_matriz()
    print("Menos conectado:")
    ar,ammo = g2.least_connected()
    print(ar,end=" ")
    print("com grau",ammo,"\n")
    print("Mais conectado:")
    ar,ammo = g2.most_connected()
    print(ar,end=" ")
    print("com grau",ammo,"\n")

    g2.grau_vertices()
    
    print("subgs:\n")
    sg2=graph.sub_grafos()
    g2.print_subgrafos(sg2)
    gc,gcm = g2.conexo()
    print("gc",gc,"gcm",gcm)


    print("\n\n========================\n========================\n\n       Caso3:     \n\n========================\n========================\n\n")

    g3=Graph("g_direc",True)
    n4=g3.add_node('a1')
    n5=g3.add_node('a2')
    n6=g3.add_node('a3')
    e5=g3.add_edge(n4,n4)
    e6=g3.add_edge(n4,n5)
    e7=g3.add_edge(n4,n6)
    e8=g3.add_edge(n5,n6)

    g3.print()
    g3.print_matriz()
    print("Menos conectado:")
    ar,ammo = g3.least_connected()
    print(ar,end=" ")
    print("com grau",ammo,"\n")
    print("Mais conectado:")
    ar,ammo = g3.most_connected()
    print(ar,end=" ")
    print("com grau",ammo,"\n")

    g3.grau_vertices()
    
    print("subgs:\n")
    sg3=g3.sub_grafos()
    g3.print_subgrafos(sg3)
    gc,gcm = g3.conexo()

    print("\n\n\n")


