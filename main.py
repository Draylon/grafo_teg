
from Graph import Graph

if __name__ == "__main__":
    '''print("\n\n========================\n========================\n\n       Caso1:     \n\n========================\n========================\n\n")

    graph=Graph()
    n1=graph.add_node('a1')
    n2=graph.add_node('a2')
    n3=graph.add_node('a3')
    e1=graph.add_edge(n1,n1)
    e2=graph.add_edge(n1,n2)
    e3=graph.add_edge(n1,n3)
    e4=graph.add_edge(n2,n3)

    
    print("\n\n========================\n========================\n\n       Caso2:     \n\n========================\n========================\n\n")
    
    graph=Graph.complemento(graph)

    print("\n\n========================\n========================\n\n       Caso3:     \n\n========================\n========================\n\n")

    graph=Graph("g_direc",True)
    n4=graph.add_node('a1')
    n5=graph.add_node('a2')
    n6=graph.add_node('a3')
    e5=graph.add_edge(n4,n4)
    e6=graph.add_edge(n4,n5)
    e7=graph.add_edge(n4,n6)
    e8=graph.add_edge(n5,n6)

    '''

    print("\n\n========================\n========================\n\n       Caso4:     \n\n========================\n========================\n\n")


    graph=Graph()
    n1=graph.add_node('a1')
    n2=graph.add_node('a2')
    n3=graph.add_node('a3')
    n4=graph.add_node('a4')
    n5=graph.add_node('a5')
    n6=graph.add_node('a6')
    n7=graph.add_node('a7')
    graph.add_edge(n1,n2)
    graph.add_edge(n1,n3)
    graph.add_edge(n2,n3)
    graph.add_edge(n3,n4)
    graph.add_edge(n4,n5)
    graph.add_edge(n5,n6)
    graph.add_edge(n5,n7)
    graph.add_edge(n6,n7)
    graph.add_edge(n7,n4)

    '''graph=Graph()
    n1=graph.add_node()
    n2=graph.add_node()
    n3=graph.add_node()
    n4=graph.add_node()
    graph.add_edge(n1,n2)
    graph.add_edge(n1,n3)
    graph.add_edge(n1,n4)
    graph.add_edge(n4,n2)
    graph.add_edge(n4,n3)'''

    '''graph=Graph()
    n0=graph.add_node()
    n1=graph.add_node()
    n2=graph.add_node()
    n3=graph.add_node()
    n4=graph.add_node()
    graph.add_edge(n0,n1)
    graph.add_edge(n0,n2)
    graph.add_edge(n2,n1)
    graph.add_edge(n1,n4)
    graph.add_edge(n4,n3)
    graph.add_edge(n3,n1)'''

    graphcomp = Graph.complemento(graph)

    
    '''graph=Graph()
    n0=graph.add_node()
    n1=graph.add_node()
    n2=graph.add_node()
    n3=graph.add_node()
    n4=graph.add_node()
    graph.add_edge(n0,n1)
    graph.add_edge(n0,n2)
    graph.add_edge(n2,n1)
    graph.add_edge(n1,n4)
    graph.add_edge(n4,n3)
    graph.add_edge(n3,n1)
    graph.add_edge(n4,n2)'''
    
    '''graph=Graph()
    n0=graph.add_node()
    n1=graph.add_node()
    n2=graph.add_node()
    graph.add_edge(n0,n1)
    graph.add_edge(n0,n2)'''
    

    graphcomp.print()
    graphcomp.print_matriz()

    ls_c = graph.ciclos()
    if graph.ciclico(ls_c) == True:
        print("Grafo ciclico")
    else:
        print("Grafo aciclico")

    print("Ciclos:")
    Graph.print_ciclos(ls_c)

    pontes_ = graph.pontes(ls_c)
    print("Pontes")
    Graph.print_pontes(pontes_)

    

    
    '''for item in ls_c:
        if item['loop'] == True:
            
            print("Edges:",end="")
            for nn in item['edges']:
                print(nn.name,end=" ")
            print("")
        print("")'''

    print("\n\n\n")


