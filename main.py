
from Graph import Graph

if __name__ == "__main__":
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
    print(graph.least_connected())
    print("Mais conectado:")
    print(graph.most_connected())
    print("subgs:\n")
    sg1=graph.sub_grafos()
    print("First:",len(sg1))
    for x1,nl in enumerate(sg1):
        print(str((x1+1))+"° conjunto:")
        for nd in nl:
            print(nd.name,end=" ")
        print("")
    print("")
    
    gc,gcm = graph.conexo()
    if gc == True:
        print("Grafo conexo, com",gcm,"subconjunto")
    else:
        print("Grafo disconexo, com",gcm,"subconjuntos")


    print("\n\n========================\n========================\n========================\n\n")
    
    g2=Graph.complemento(graph)
    g2.print()
    g2.print_matriz()
    print("Menos conectado:")
    print(g2.least_connected())
    print("Mais conectado:")
    print(g2.most_connected())
    print("subgs:\n")
    for x1,nl in enumerate(g2.sub_grafos()):
        print(str((x1+1))+"° conjunto:")
        for nd in nl:
            print(nd.name,end=" ")
        print("")
    print("")

    gc,gcm = g2.conexo()
    if gc == True:
        print("Grafo conexo, com",gcm,"subconjunto")
    else:
        print("Grafo disconexo, com",gcm,"subconjuntos")