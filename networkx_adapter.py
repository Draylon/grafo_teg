import networkx as nx
import matplotlib.pyplot as plt
#from Graph import Graph
from Edge import Edge
from Node import Node

def create_networkx_graph(grafo):
    g = None
    if grafo.is_directed():
        g = nx.DiGraph()
    else:
        g = nx.Graph()
    g.name =grafo.name
    for node in grafo.get_nodes():
        g.add_node(node)
    for from_ in grafo.get_nodes():
        for edge_,dest_ in grafo.get_connections(from_).items():
            '''if from_.id > dest_.id:
                continue'''
            g.add_edge(from_, dest_, weight=edge_.weight, name=edge_.name)
    return g

    #H = nx.relabel_nodes(g, grafo.get_node_dictionary())

def networkx_draw(nx_grafo,edge_list,custom_pos={},no_edge_label=False):
    #top = nx.bipartite.sets(nx_grafo)[0]
    #pos = nx.bipartite_layout(nx_grafo, top)
    #nx.draw(nx_grafo, with_labels=True)
    #nx.draw(nx_grafo, pos, with_labels=True)
    # plt.savefig("path_graph_cities.png")
    #plt.show()

    #edges = [['A', 'B'], ['B', 'C'], ['B', 'D']]
    edg_labels = {}
    for nge in nx_grafo.edges:
        edg_labels[nge] = edge_list[nge[0]][nge[1]].name

    #pos = nx.spring_layout(G,15)
    pos = {}
    if len(custom_pos) > 0:
        for np,nd in enumerate(nx_grafo.nodes):
            pos[nd] = custom_pos[np]
    else:
        pos = nx.spring_layout(nx_grafo)
        
    plt.figure()
    plt.title(nx_grafo.name)
    nx.draw(nx_grafo, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='gray', alpha=0.9,
            labels={node: node for node in nx_grafo.nodes()},connectionstyle='arc3, rad = 0.1')
    #nx.draw_networkx_edge_labels(G, pos, edge_labels={('A', 'B'): 'AB',('B', 'C'): 'BC', ('B', 'D'): 'BD'}, font_color='red')
    if not no_edge_label:
        nx.draw_networkx_edge_labels(nx_grafo, pos, edge_labels=edg_labels, font_color='red',label_pos=0.3)
    #nx.draw(G,pos,connectionstyle='arc3, rad = 0.1',with_labels=True)
    plt.axis('off')

    plt.show()