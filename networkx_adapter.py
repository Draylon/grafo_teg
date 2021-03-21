import networkx as nx
import matplotlib.pyplot as plt
from Graph import Graph
from Edge import Edge
from Node import Node

def create_networkx_graph(grafo=Graph()):
    g = nx.Graph()
    for node in grafo.get_nodes():
        g.add_node(node)
    for from_ in grafo.get_nodes():
        for edge_,dest_ in grafo.get_connections(from_).items():
            g.add_edge(from_,dest_,weight=edge_.weight)
    return g

    #H = nx.relabel_nodes(g, grafo.get_node_dictionary())

def networkx_draw(nx_grafo):
    #top = nx.bipartite.sets(nx_grafo)[0]
    #pos = nx.bipartite_layout(nx_grafo, top)
    nx.draw(nx_grafo, with_labels=True)
    #nx.draw(nx_grafo, pos, with_labels=True)
    # plt.savefig("path_graph_cities.png")
    plt.show()