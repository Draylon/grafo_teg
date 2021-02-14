from Graph import Graph

if __name__ == "__main__":
    graph=Graph()
    node1=graph.add_node("n1")
    node2=graph.add_node('n2')
    node3=graph.add_node('n3')
    edge1=graph.add_edge(node1,node2)
    edge2=graph.add_edge(node1,node3)
    graph.print()