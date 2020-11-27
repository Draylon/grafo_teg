
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
    graph.print_subgrafos(sg1)
    gc,gcm = graph.conexo()
    print("gc",gc,"gcm",gcm)
    


    print("\n\n========================\n========================\n========================\n\n")
    
    g2=Graph.complemento(graph)
    g2.print()
    g2.print_matriz()
    print("Menos conectado:")
    print(g2.least_connected())
    print("Mais conectado:")
    print(g2.most_connected())
    
    print("subgs:\n")
    sg2=graph.sub_grafos()
    g2.print_subgrafos(sg2)
    gc,gcm = g2.conexo()
    print("gc",gc,"gcm",gcm)

    print("\n\n\n")