from Node import Node
from Edge import Edge
from Queue import MQueue
from Stack import MStack
import decimal

INF = float("inf")
# noinspection SpellCheckingInspection
class Graph:
    def __init__(self, name=None, direcionado=False,createMatrix=True,createList=True):
        if name:
            self.name = name
        else:
            self.name = "Graph"
        self.__direcionado = direcionado
        self.__nodes = []
        self.__edges = {}
        if createList == True: # criar elementos de lista
            self.__connections = {} # { Node: { Edge: Node } }
            self.__node_conns = {} # { Node: { Node: Edge } } conexões listadas por pares de nodes
            self.__visited_node = {} # { Node: Bool }
            self.__visited_edge = {} # { Edge: Bool }
            self.__node_name = {} # { String: Node } relacionar node ao nome
        self.__edge_count=0 # contador de arestas
        self.__node_count=0 # contador de nó

        # == criando matriz ==
        # self.__matrix = [[0 for y in range(self.numVerticesMaximo)] for x in range(self.numVerticesMaximo)]
        if createMatrix == True:
            self.matrix = [] # melhor colocar lista vazia

    def __del__(self):
        self.__nodes.clear()
        self.__edges.clear()
        self.__connections.clear()
        self.__node_conns.clear()
        self.__visited_edge.clear()
        self.__visited_node.clear()
        # print("Graph",self.name,"Deleted!")
    # ==============================
    #
    # Funções de auxílio para as operações
    #
    # ==============================

    def is_directed(self):
        return self.__direcionado

    #Adicionar Node

    def __setup_node(self,n):
        self.__nodes.append(n)
        self.__node_count+=1
        # print("adding",n.name,"to graph")

        self.__new_to_matrix()
        self.__visited_node[n] = False
        self.__connections[n] = {}
        self.__node_conns[n] = {}
        self.__node_name[n.name] = n

    def add_node_object(self,node):
        self.__setup_node(node)

    def add_node(self, name=None,position=()):  # add into graph
        n = Node(self, name,position=position)
        self.__setup_node(n)
        return n

    # Fim adicionar Node

    # Remover node

    def remove_node(self, node):  # remove from graph
        if node is None or node is False:
            return
        try:
            if self.__edges == {} or self.__nodes == []:
                return
            # print("removing",node.name,"from",self.name)
            ind = self.__nodes.index(node)
            self.__remove_from_matrix(ind)
            self.disconnect_node(node)
            self.__nodes.pop(ind)
            self.__visited_node.pop(node)
            self.__connections.pop(node)
            self.__node_conns.pop(node)

        except Exception as _:
            pass
            # print("error removing node",exp)


    def disconnect_node(self, node):  # delete all edges
        """Desconectar um node sem excluir"""
        ind = self.__nodes.index(node)
        for edge, _ in self.__visited_node[node].items():
            del edge
        self.__zero_matrix_at(ind)
        for ed, dstn in self.__connections[node].items():
            if dstn == node:
                self.remove_edge(ed)

    def get_index_from_node(self, node):
        """pegar index do node no dicionario"""
        try:
            return self.__nodes.index(node)
        except ValueError as _:
            return -1

    def get_node_from_index(self, index):
        """pegar node do dicionario via índice"""
        return self.__nodes[index]

    
    def get_node_dictionary(self):
        """construir um dicionário de indice: Node"""
        dicct = {}
        for i,e in enumerate(self.__nodes):
            dicct[i]=e
        return dicct


    def get_node_by_name(self,name):
        """Buscar node pela estrutura de nome"""
        return self.__node_name.get(name,None)

    def get_nodes(self):
        """Retornar o dicionário de Nodes"""
        return self.__nodes
    
    def get_graph_order(self):
        """Ordem do grafo (Quantos Nodes tem)"""
        return self.__node_count

    #==============================================
    #========     Operações em arestas     ========
    #==============================================
    
    def get_edges(self): return list(self.__edges.keys())

    def get_edge(self, node1, node2):
        if self.__direcionado is True:
            return self.__node_conns[node1].get(node2,None)
        else:
            if self.__node_conns[node1].get(node2,None) == None:
                return self.__node_conns[node2].get(node1,None)
            else:
                return self.__node_conns[node1].get(node2,None)


    def get_edge_count(self):
        return self.__edge_count

    def get_edge_from_index(self,index):
        return list(self.__edges.keys())[index]

    def get_nodes_from_edge(self,edge):
        if self.__node_conns:
            for from_,data_ in self.__node_conns.items():
                for dest_,edge_ in data_.items():
                    if edge_ == edge:
                        return from_,dest_
            return None,None
        else: return None,None

    def get_connections(self, node):
        """Todas as adjacências do Node"""
        return self.__connections.get(node,None)
        

    def get_node_connections(self):return self.__node_conns

    #======================================================
    #========     Operações na parte de matriz     ========
    #======================================================

    """Desconecta um node"""
    def __zero_matrix_at(self, index):
        ic = 0
        while ic < index:
            self.matrix[ic][index] -= 1
            ic += 1
        ic += 1
        while ic < len(self.matrix):
            self.matrix[ic][index] -= 1
            ic += 1
        self.matrix[index] = [0 for n in range(len(self.__nodes))]


    """Remove um elemento da matriz (linha e coluna)"""
    def __remove_from_matrix(self, index):
        ic = 0
        while ic < index:
            self.matrix[ic].pop(index)
            ic += 1
        ic += 1
        while ic < len(self.matrix):
            self.matrix[ic].pop(index)
            ic += 1
        self.matrix.pop(index)

    """Aumenta a matriz em uma linha e uma coluna"""
    def __new_to_matrix(self):
        r = len(self.matrix)
        for n in range(r):
            self.matrix[n].append(0)
        self.matrix.append([0 for tt in range(r + 1)])

    def __update_to_matrix(self, i, j, val):
        self.matrix[i][j] += val
        if self.__direcionado is False and i != j: self.matrix[j][i] += val

    def next_node(self, node, edge):
        """Node adjacente de uma Aresta"""
        return self.__connections[node].get(edge,None)
        
    def __edge_op(self,node1,node2,l1,l2,e):
        self.__update_to_matrix(l1, l2, 1)

        self.__connections[node1][e] = node2
        self.__node_conns[node1][node2]=e
        self.__edges[e] = node1
        if self.__direcionado == False and node1 != node2:
            self.__connections[node2][e] = node1
            self.__node_conns[node2][node1]=e

        self.__visited_edge[e] = False
        

    def add_edge_object(self,edge):
        nodes = self.get_nodes_from_edge(edge)
        self.__edge_op(nodes[0],nodes[1],self.__nodes.index(nodes[0]),self.__nodes.index(nodes[1]),edge)

    def add_edge(self, node1, node2, name=None,capacidade=0,fluxo=0,add_parallel=False):
        if node1 not in self.__nodes or node2 not in self.__nodes:
            return None
        l1 = self.__nodes.index(node1)
        l2 = self.__nodes.index(node2)
        e = None
        if name==None:
            name = node1.name+"_"+node2.name
        
        if self.get_edge(node2,node1) is not None:
            e = Edge(self, 1, name, self.__direcionado,capacidade,fluxo,True)
        else:
            e = Edge(self, 1, name, self.__direcionado,capacidade,fluxo,False)
        
        self.__edge_op(node1,node2,l1,l2,e)
        if not add_parallel:
            return e
        else: return [e,self.add_edge(node2,node1,name,capacidade,fluxo,False)]

    def __add_edge_man(self, node1, node2, xi, yi, name=None):
        if name==None:
            name = node1.name+"_"+node2.name
        e = Edge(self, 1, name, self.__direcionado)
        self.__connections[node1][e] = node2
        self.__node_conns[node1][node2] = e
        self.__edges[e] = node1
        if self.__direcionado == False and xi != yi:
            self.__connections[node2][e] = node1
            self.__node_conns[node2][node1] = e
        self.__visited_edge[e] = False
        return e

    def remove_edge(self, edge):
        # print("removing",edge.name,"from",self.name)
        try:
            if self.__edges == {} or self.__nodes == []:
                return
            from_ = self.__edges[edge]
            to_ = self.__connections[from_][edge]
            self.__connections[from_].pop(edge)
            self.__connections[to_].pop(edge)
            self.__node_conns[from_].pop(to_)
            self.__visited_edge.pop(edge)
            self.__edges.pop(edge)
        except Exception as exp:
            print("error removing edge", edge.name, "\nerr:", exp)

    def __clear_visited_nodes(self):
        for n in self.__visited_node.keys():
            self.__visited_node[n] = False

    def __clear_visited_edges(self):
        for e in self.__visited_edge.keys():
            self.__visited_edge[e] = False

    def __get_all_connected_edges(self,node):
        edges = []
        for from_,data in self.__node_conns.items():
            for dest,edge in data.items():
                if from_ == node or dest == node:
                    edges.append(edge)
        return edges
    
    def __get_all_connected_nodes(self,node):
        nodes = set()
        for from_,data in self.__node_conns.items():
            if from_ == node:
                for dest,_ in data.items():
                    nodes.add(dest)
            else:
                for dest,_ in data.items():
                    if node == dest:
                        nodes.add(from_)
                    
        return nodes

    #====================================
    
    #===========   FUNCOES   ============
    
    #====================================

    def adjacente(self,node1,node2):
        if self.__node_conns[node1].get(node2,False) != False:
            return True
        return False

    def completo(self):
        for data in self.__connections.values():
            if data == {}:
                return False
        return True

    def grau_vertice(self, index):
        if type(index) != int:
            index = self.get_index_from_node(index)
        grau = 0
        for xi, x in enumerate(self.matrix[index]):
            grau += 2 * x if xi == index else x
        return grau

    def coloracao(self):
        self.__clear_visited_nodes()
        known_colors = set()
        for node in self.__nodes:
            connected_colors = set()
            for dest in self.__get_all_connected_nodes(node):
                if type(self.__visited_node[dest]) != bool:
                    connected_colors.add(self.__visited_node[dest])
            num_color = -1
            try:
                num_color = min(known_colors - connected_colors)
            except ValueError as _:
                num_color = len(known_colors)
                known_colors.add(num_color)
            self.__visited_node[node] = num_color
            
        return self.__visited_node.copy()

    def bipartido(self, node_init):
        matrix_len = len(self.__nodes)
        init_index = self.get_index_from_node(node_init)
        b_colors = [-1] * matrix_len
        b_colors[init_index] = 1
        b_queue = [init_index]
        while b_queue:
            dest_ = b_queue.pop()
            if self.matrix[dest_][dest_] == 1:
                return False
            for i in range(matrix_len):
                if self.matrix[dest_][i] == 1 and b_colors[dest_] == -1:
                    b_colors[i] = 1 - b_colors[dest_]
                    b_queue.append(dest_)
                elif self.matrix[dest_][i] == 1 and b_colors[i] == b_colors[dest_]:
                    return False
        return True

    #  ======    Bugado   ==========#
    #  ======    Bugado   ==========#
    """def bipartido3(self):
        self.__clear_visited_nodes()
        set1 = set()
        set2 = set()
        for node in self.__nodes:
            self.__visited_node[node]=True
            set1.add(node)
            for _,dest in self.__connections[node].items():
                if not self.__visited_node[dest]:
                    self.__visited_node[dest]=True
                    set2.add(dest)
        return set1.intersection(set2)"""

    def bipartido2(self):
        get_ = self.coloracao()
        for _,i in get_.items():
            if i > 1:
                return False
        return True


    def planar(self,list_grau_conexoes):
        try:
            if list_grau_conexoes[(4, 4)] >= 20: # Tem um k5
                return False
        except Exception as _:
            pass

        try:
            if list_grau_conexoes[(3,3)] >= 18: # Tem um k3,3
                return False
        except Exception as _:
            pass
        return True

    

    def __pathing_rec(self, current, arrival,last=None,
        allow_visited_edges=False,allow_visited_nodes=False,
        allow_return_edge=False, edge_list=[None],depth=0):
        """Iterador de caminhos entre dois Nodes, usado em varias partes do código
        Usando iteração recursiva, para reproduzir BFS
        """
        if self.__visited_node[current] == True and not allow_visited_nodes: # node já visitado
            return
        for edge, dest_ in self.__connections[current].items():
            if not allow_return_edge and edge.parallel==True:
                continue
            if self.__visited_edge[edge] == True and not allow_visited_edges:
                continue
            edge_list[depth]=edge
            if not allow_visited_edges: self.__visited_edge[edge] = True
            if not allow_visited_nodes: self.__visited_node[current] = True
            if dest_ == arrival:
                #edge_list = edge_list[:-1]
                #edge_list.append(dest_)
                #print(edge_list[:depth+1])
                self.__pathing_list.append(edge_list[:depth+1])
                #return
                #break
            else:
                edge_list.append(None)
                self.__pathing_rec(dest_, arrival,current,allow_visited_edges,allow_visited_nodes,allow_return_edge,edge_list,depth+1)

    #==========================
    # Buscar caminhos com menor peso
    def max_weight(self, departure, arrival):
        """Caminho de peso máximo"""
        if departure not in self.__nodes or arrival not in self.__nodes:
            return -1
        self.__pathing_list = []
        self.__pathing_rec(departure, arrival)
        self.__clear_visited_edges()
        longest_path = -1
        for path in self.__pathing_list:
            path_weight = 0
            for edge in path:
                path_weight = path_weight + edge.weight
            if path_weight > longest_path:# or longest_path == -1:
                longest_path = path_weight
        del self.__pathing_list
        return longest_path


    def min_weight(self, departure, arrival):
        """Caminho de peso mínimo"""
        if departure not in self.__nodes or arrival not in self.__nodes:
            return -1
        self.__pathing_list = []
        self.__pathing_rec(departure, arrival)
        shortest_path = -1
        for path in self.__pathing_list:
            path_weight = 0
            for edge in path:
                path_weight = path_weight + edge.weight
            if path_weight < shortest_path or shortest_path == -1:
                shortest_path = path_weight
        del self.__pathing_list
        return shortest_path

    #=============================

    def most_connected(self):
        """Lista de índices dos nodes MAIS conectados, e o grau deles"""
        most_ = []
        ammo, xn = -1, 0
        for xi, x in enumerate(self.matrix):
            new_ammo = 0
            for yi, y in enumerate(x):
                new_ammo += 2 * y if xi == yi else y
            if new_ammo == ammo:
                most_.append(xn)
            if new_ammo > ammo or ammo == -1:
                most_ = [xn]
                ammo = new_ammo

            xn += 1
        return most_, ammo

    def least_connected(self):
        """Lista de índices dos nodes MENOS conectados, e o grau deles"""
        most_ = []
        ammo, xn = -1, 0
        for xi, x in enumerate(self.matrix):
            new_ammo = 0
            for yi, y in enumerate(x):
                new_ammo += 2 * y if xi == yi else y
            if new_ammo == ammo:
                most_.append(xn)
            if new_ammo < ammo or ammo == -1:
                most_ = [xn]
                ammo = new_ammo

            xn += 1
        return most_, ammo

    def most_connected_objects(self):
        """Mais conectados, usando as listas"""
        ind_l, ammo = self.most_connected()
        nodes = []
        for ind in ind_l:
            nodes.append(self.get_node_from_index(ind))
        return nodes, ammo

    def least_connected_objects(self):
        """Menos conectados, usando as listas"""
        ind_l, ammo = self.least_connected()
        nodes = []
        for ind in ind_l:
            nodes.append(self.get_node_from_index(ind))
        return nodes, ammo

    def bfs_print(self,start=None):
        if start == None:
            start = self.__nodes[0]
        """estrutura da lista de adjacencias(connections): 
        dict({
            Node: dict({Edge: Node})
        })
        """
        self.__clear_visited_nodes()
        self.__visited_node[start] = True
        queue = MQueue()
        queue.push(start)

        while queue.not_empty():
            node = queue.pop()
            for _,dest in self.__connections[node].items(): # lista de adjacências
                if self.__visited_node[dest] == False:
                    self.__visited_node[dest] = True
                    queue.push(dest)
            print("node",node)

    # sub grafos
    def sub_grafos(self):
        self.__sub_grafl = [[]]
        nc = 0
        for node in self.__nodes:
            if self.__visited_node[node] == False:
                self.__sub_grafos_rec(nc, node)
                nc += 1
                self.__sub_grafl.append([])
        self.__sub_grafl.pop()
        self.__clear_visited_nodes()
        return self.__sub_grafl.copy()

    def __sub_grafos_rec(self, curr, node):
        if self.__visited_node[node] == False:
            self.__sub_grafl[curr].append(node)
            self.__visited_node[node] = True
            for _, dest_ in self.__connections[node].items():
                self.__sub_grafos_rec(curr, dest_)
        return

    # pontes 
    def pontes(self, lista_ciclos):
        """Listar as arestas-Ponte no grafo que contém ciclos"""
        edge_cycle = set()
        self.__clear_visited_edges()
        for nd_list in lista_ciclos:
            for nd in nd_list:
                for edg, dest1 in self.__connections[nd].items():
                    if dest1 in nd_list:
                        self.__visited_edge[edg] = True
        for edg, bool_ in self.__visited_edge.items():
            if bool_ == False:
                edge_cycle.add(edg)
        return edge_cycle


    # arvores
    def arvore(self, lista_ciclos):
        """Define se o gráfo é do tipo árvore"""
        if (not ciclico(lista_ciclos) and self.conexo()[0] == True):
            return True
        else:
            return False



    # Algoritmo Cíclos "Funcionando"

    def __ciclos_bfs(self,node_queue):
        """Construir uma árvore de iteração dos Nodes apartir de uma fila"""
        while node_queue.not_empty():
            node = node_queue.pop()
            self.__visited_node[node]=True
            #print("\npopped",node)
            #self.__ciclos_def(node,level,parent)
            
            for _,d in self.__connections[node].items():
                if self.__visited_node[d] == False:
                    #print(node,"has",d,"to go")
                    self.__visited_node[d] = True
                    node_queue.push(d)
                    try:
                        self.__cycle_node_data[d][1].add(node)
                    except Exception as _:
                        self.__cycle_node_data[d] = [self.__cycle_node_data[node][0]+1,{node}]
                    
                    try:
                        self.__parentnode_data[node].add(d)
                    except Exception as _:
                        self.__parentnode_data[node] = {d}
                    try:
                        self.__level_node_data[self.__cycle_node_data[node][0]+1].add(d)
                    except Exception as _:
                        self.__level_node_data[self.__cycle_node_data[node][0]+1] = set([d])
        #return cycle_node_data,level_node_data,parentnode_data

    def __cycle_rec(self,node):
        for samelevel in self.__level_node_data[self.__cycle_node_data[node][0]]:
            if node != samelevel:
                
                if self.__node_conns[node].get(samelevel,None) != None:
                    #print("\n")
                    #print(node,"connected to same level as",samelevel)
                    test_same_parent = self.__cycle_node_data[node][1].intersection(self.__cycle_node_data[samelevel][1])
                    if len(test_same_parent) > 0:
                        #print("    ",node,"and",samelevel,"have common parents")
                        test_same_parent.add(node)
                        test_same_parent.add(samelevel)
                        #print("    added cycle",test_same_parent)
                        self.__cycle_list.add(frozenset(test_same_parent))
                    else:
                        #print("    ",node,"and",samelevel,"come from different parents")
                        add_list=set()
                        node1 = self.__cycle_node_data[node][1]
                        node2 = self.__cycle_node_data[samelevel][1]
                        for n1p in node1:
                            for n2p in node2:
                                if n1p == n2p:
                                    #cycle - n1p samelevel node
                                    add_list.add(n1p)
                                    add_list.add(samelevel)
                                    #print("        cycle -",add_list)
                                    self.__cycle_list.add(frozenset(add_list))
                                    add_list.clear()
                                else:
                                    has_cross=False
                                    #print("        checking cross",node,n2p)
                                    if self.__node_conns[node].get(n2p,None) != None:
                                        #print("        node connected to cross level 1",node,n2p,samelevel)
                                        #parents connected
                                        #cycle - n1p n2p node samelevel
                                        add_list.add(node)
                                        add_list.add(samelevel)
                                        add_list.add(n2p)
                                        print("        cycle -",add_list)
                                        self.__cycle_list.add(frozenset(add_list))
                                        add_list.clear()
                                        has_cross=True
                                    
                                    #print("        checking cross",n1p,samelevel)
                                    if self.__node_conns[n1p].get(samelevel,None) != None:
                                        #print("        node connected to cross level 2",node,n1p,samelevel)
                                        #parents connected
                                        #cycle - n1p n2p node samelevel
                                        add_list.add(node)
                                        add_list.add(n1p)
                                        add_list.add(samelevel)
                                        print("        cycle -",add_list)
                                        self.__cycle_list.add(frozenset(add_list))
                                        add_list.clear()
                                        has_cross=True
                                    
                                    
                                    if has_cross == False and self.__node_conns[n1p].get(n2p,None) != None:
                                        #print("        parents connected",n1p,n2p)
                                        #parents connected
                                        #cycle - n1p n2p node samelevel
                                        add_list.add(n1p)
                                        add_list.add(n2p)
                                        add_list.add(samelevel)
                                        #print("        cycle -",add_list)
                                        self.__cycle_list.add(frozenset(add_list))
                                        add_list.clear()
                                    else:
                                        #parents not connected
                                        add_list.add(n1p)
                                        add_list.add(n2p)
                else:
                    #print("\n")
                    #print(node,"same level but not connected to",samelevel)
                    pass
        
        if self.__cycle_node_data[node][0] > 0:
            add_list = set()
            
            #print("\nadding",node)
            add_list.add(node)
            node1pl = self.__cycle_node_data[node][1]
            node2l = self.__level_node_data[self.__cycle_node_data[node][0]-1]
            #print("nodes no nivel anterior ao",node,": ",node2l)
            
            
            for parentlevel in node2l:
                if parentlevel not in node1pl:
                    #print("    testando entre",node,"e",parentlevel)
                    if self.__node_conns[node].get(parentlevel,None) != None:
                        #print("        ",node,"conectado ao",parentlevel)
                        for n1p in node1pl:
                            if self.__node_conns[n1p].get(parentlevel,None) != None:
                                #print("            parent do",node,"conectado ao",parentlevel)
                                add_list.add(n1p)
                                add_list.add(parentlevel)
                                add_list.add(node)
                                #print("            cycle -",add_list)
                                self.__cycle_list.add(frozenset(add_list))
                                add_list.clear()
                                #parents connected - cycle
                            else:
                                #print("            parent do",node,"{",n1p,"} nao conecta com",parentlevel)
                                add_list.add(parentlevel)
                                breaker=False
                                temp_1={n1p}
                                temp_2={parentlevel}
                                add_list.add(n1p)
                                add_list.add(parentlevel)
                                while not breaker:
                                    #print("buscando com",temp_1,"e",temp_2)
                                    for temp1 in temp_1:
                                        for temp2 in temp_2:
                                            temp_1l=self.__cycle_node_data[temp1][1]
                                            temp_2l=self.__cycle_node_data[temp2][1]
                                            if len(temp_1l.intersection(temp_2l)) > 0:
                                                #print(temp_1l,"e",temp_2l,"pararam no mesmo nivel, logo tem o mesmo pai")
                                                for t1l in temp_1l:
                                                    add_list.add(t1l)
                                                breaker=True
                                            else:
                                                #print("ainda nao encontrou entre",temp_1l,"e",temp_2l)
                                                for t1l in temp_1l:
                                                    add_list.add(t1l)
                                                for t1l in temp_2l:
                                                    add_list.add(t1l)
                                                temp_1 = self.__cycle_node_data[temp1][1]
                                                temp_2 = self.__cycle_node_data[temp2][1]
                                #print("add_list = ",add_list)
                                self.__cycle_list.add(frozenset(add_list))
                                add_list.clear()
                    else:
                        #print("        ",node,"nao conecta com",parentlevel)
                        pass
                else:
                    #print("    ",node2l,"contem o pai de",node,"que é",node1pl)
                    pass
        try:
            for dest in self.__parentnode_data[node]:
                self.__cycle_rec(dest)
        except Exception as _:
            pass

        
        
    def ciclos(self):
        self.__clear_visited_nodes()
        node_queue = MQueue()
        self.__cycle_list = set()
        self.__cycle_node_data = {}
        self.__parentnode_data = {}
        self.__level_node_data = {}
        node = self.__nodes[0]
        if len(self.__nodes) > 0:
            node_queue.push(node)
            self.__cycle_node_data[node] = [0,set()]
            self.__level_node_data[0] = set([node])
            self.__visited_node[node] = True
            self.__cycle_node_data[node] = [0,{None}]
            
        self.__ciclos_bfs(node_queue)
        print("Done tree")
        print(self.__cycle_node_data)
        print(self.__parentnode_data)
        print(self.__level_node_data)
        print("\n")
        self.__cycle_rec(node)
        

        """for level,nodes in level_node_data.items():
            repeat_list = {}
            for node1 in nodes:
                
                #Procurar no mesmo nível
                #Procurar No nivel anterior, não no mesmo pai
                level_b = level
                print("node",node1,"level",level)
                while level_b >= 0:
                    for node2 in level_node_data[level_b]:
                        try:
                            if repeat_list[self.__node_conns[node1][node2]] == True:
                                print("Already done",node1,node2)
                                pass
                        except Exception as _:
                            #print(e)
                            try:
                                if self.__node_conns[node1][node2] and node1 != node2 and not parentnode_data[node2].__contains__(node1):
                                    repeat_list[self.__node_conns[node1][node2]] = True
                                    print(node1,"is connected to",node2)
                                    
                                    common_parents = cycle_node_data[node1][1].intersection(cycle_node_data[node2][1])
                                    if len(common_parents) > 0:
                                        if len(common_parents) > 0:
                                            common_parents.add(node1)
                                            common_parents.add(node2)
                                            print("cycle",common_parents)
                                            cycle_list.add(frozenset(common_parents))

                                    else:
                                        cycle_=False
                                        for n1p in cycle_node_data[node1][1]:
                                            try:
                                                if self.__node_conns[n1p][node2]:
                                                    cycle_list.add({n1p,node2,node1})
                                                    cycle_=True
                                                    break
                                            except Exception as _:
                                                pass
                                        if not cycle_:
                                            for n2p in cycle_node_data[node2][1]:
                                                try:
                                                    if self.__node_conns[n2p][node1]:
                                                        cycle_list.add({n2p,node2,node1})
                                                        cycle_=True
                                                        break
                                                except Exception as _:
                                                    pass
                                        if not cycle_:
                                            breaker=False
                                            add_list=set()
                                            n1pl = cycle_node_data[node1][1]
                                            n2pl = cycle_node_data[node2][1]
                                            while not breaker:
                                                l1m,l2m=set(),set()
                                                for n1p in n1pl:
                                                    if n1p==None:
                                                        breaker=True
                                                        continue
                                                    l1m.update(cycle_node_data[n1p][1])
                                                    for n2p in n2pl:
                                                        if n2p==None:
                                                            breaker=True
                                                            continue
                                                        l2m.update(cycle_node_data[n2p][1])
                                                        try:
                                                            if n1p == n2p:
                                                                add_list.add(node1)
                                                                add_list.add(node2)
                                                                add_list.add(n1p)
                                                                cycle_list.add(frozenset(add_list))
                                                                add_list.clear()
                                                                breaker=True
                                                            elif self.__node_conns[n1p][n2p]:
                                                                add_list.add(node1)
                                                                add_list.add(node2)
                                                                add_list.add(n1p)
                                                                add_list.add(n2p)
                                                                cycle_list.add(frozenset(add_list))
                                                                add_list.clear()
                                                                breaker=True
                                                        except Exception as _:
                                                            #print(e)
                                                            #parents not connected
                                                            add_list.add(n1p)
                                                            add_list.add(n2p)
                                                n1pl=l1m
                                                n2pl=l2m




                                        add_list = set()
                                        #which parents actually communicate with node1
                                        for linked_parent in cycle_node_data[node1][1]:
                                            print("Linked",node1,"to",linked_parent)
                                            try:
                                                if self.__node_conns[node1][linked_parent]:
                                                    #direct connection
                                                    add_list.add(linked_parent)
                                                    add_list.add(node1)
                                                    add_list.add(node2)
                                                    print("cycle",add_list)
                                                    cycle_list.add(frozenset(add_list))
                                                    add_list.clear()
                                            except Exception as _:
                                                print("extension",linked_parent)
                                                add_list.add(linked_parent)
                                                #extension ( possibly not connected to other on same level)
                                           

                                    
                            except Exception as _:
                                pass
                        
                    level_b-=1"""
                    
        print("cycles:",self.__cycle_list)

    def conexo(self):
        subg = self.sub_grafos()
        legc = len(subg)
        if legc == 1:
            # print("Grafo conexo, com",legc,"subconjunto")
            return True, legc
        # print("Grafo disconexo, com",legc,"subconjuntos")
        return False, legc

    def __saltos_rec(self, last, efrom, node, indc, lim, mode):
        rotas = self.get_connections(node)
        if len(rotas) == 1:
            return node, None
        else:
            for edr, desr in rotas.items():
                if desr != last:
                    if mode == 1:
                        if indc >= lim:
                            return node, self.__saltos_rec(node, edr, desr, indc, lim, mode)
                        else:
                            return self.__saltos_rec(node, edr, desr, indc + 1, lim, mode)
                    elif mode == 0:
                        if indc < lim - 1:
                            return node, self.__saltos_rec(node, edr, desr, indc + 1, lim, mode)
                        else:
                            return node, None
                    else:
                        return None
            return None

    def saltos(self, node_init, saltos, mode):
        """
            Mode: 1 = nodes que estão além do numero de saltos\n
            Mode: 0 = nodes que vão até do numero de saltos
        """
        saltos_list = []
        for edc, destc in self.get_connections(node_init).items():
            saltos_list.append(self.__saltos_rec(node_init, edc, destc, 1, saltos, mode))
        return saltos_list

    def __dfs_rec(self,init,last=None,iter=0):
        if self.__visited_node[init] < iter and self.__visited_node[init] is not False:
            return
        self.__visited_node[init] = iter
        for _,destination in self.__connections[init].items():
            if destination != last:
                self.__dfs_rec(destination,init,iter+1)

    def dfs(self, init):
        self.__clear_visited_nodes()
        self.__dfs_rec(init)
        return self.__visited_node.copy()

    def dfs_print(self,start=None):
        if start == None:
            start = self.__nodes[0]
        self.__clear_visited_nodes()
        stack = MStack()
        stack.push(start)
        while stack.not_empty():
            node = stack.pop()
            self.__visited_node[node] = True
            for _,dest in self.__connections[node].items(): # lista de adjacências
                if self.__visited_node[node] == False:
                    stack.push(dest)
            print("node",node)
    """def dfs_print(self,pathing_list):
        for index, path in enumerate(pathing_list):
            print("Caminho", index)
            for node in path:
                print(node, end=" - ")
            print("")"""

    def dfs_paths(self,departure,arrival):
        if departure not in self.__nodes or arrival not in self.__nodes:
            return -1
        self.__pathing_list = []
        self.__clear_visited_nodes()
        self.__clear_visited_edges()
        self.__pathing_rec(departure, arrival,allow_return_edge=True)
        cp1 = self.__pathing_list.copy()
        del self.__pathing_list
        return cp1

    def calcular_fluxo(self,node):
        """
        SOMAR OS FLUXOS DO VÉRTICE DE SAÍDA
        """
        fluxo=0
        for edge in self.__connections[node].keys():
            fluxo+=edge.getFlux()
        return fluxo

    def corte(self,departure,arrival,modo):
        """
        CORTE FUNCIONA ITERANDO POR TODOS OS CAMINHOS E VENDO QUAL É O
        VALOR DE FLUXO\n
        Modo = 1 => Corte máximo\n
        Modo = 0 => Corte mínimo\n
        :return:
        Edge com a capacidade selecionada ( pode ser acessado por .get_capacidade() )
        """
        if modo != 0 and modo != 1:
            raise Exception("Modo incorreto")
        if departure not in self.__nodes or arrival not in self.__nodes:
            return -1
        self.__pathing_list = []
        self.__clear_visited_edges()
        self.__pathing_rec(departure, arrival,None,True,True)
        #len_fluxos = len(self.__pathing_list)
        edges_list = set()
        for edge_l in self.__pathing_list:
            print(edge_l)
            for edge in reversed(edge_l):
                if edge.getCap() == edge.getFlux():
                    edges_list.add(edge)
                    break

        '''for path_i in range(len_fluxos): # iterando por todos os caminhos
            s_flux=None
            for sel_edge in self.__pathing_list[path_i]: # iterando por
                if modo == 0: # mínimo
                    if s_flux == None or s_flux.get_capacidade() < sel_edge.get_capacidade():
                        s_flux = sel_edge
                elif modo == 1:
                    if s_flux == None or s_flux.get_capacidade() > sel_edge.get_capacidade():
                        s_flux = sel_edge
            edges_list[path_i] = s_flux'''
        del self.__pathing_list
        return edges_list


    def print(self):
        """Printar o grafo"""
        for node in self.__nodes:
            print("Node", node.name, "\n    conectado a: ", end="")
            try:
                nn = True
                for edge, dest1 in self.__connections[node].items():
                    nn = False
                    print("(" + edge.name + "," + dest1.name + ")", end=" ")
                if nn == True: print("Nenhum", end="")
                print("\n")
            except Exception as ex:
                print("Erro", ex, "\n")
        print("")

    def print_matriz(self,modo='pesos'):
        """
        :param modo:pesos,capacidade,fluxo
        :return:
        """
        if modo == 'pesos' and modo!='capacidade' and modo!='fluxo':
            return
        print("Matriz:",modo)
        for xi,x in enumerate(self.matrix):
            for yi,y in enumerate(x):
                if modo=='pesos':
                    print(y, end=" ")
                elif modo=='capacidade':
                    if self.get_node_from_index(yi) in self.__node_conns[self.get_node_from_index(xi)]:
                        print(self.__node_conns[self.get_node_from_index(xi)][self.get_node_from_index(yi)].getCap(), end=" ")
                    else: print(-1,end=' ')
                elif modo=='fluxo':
                    if self.get_node_from_index(yi) in self.__node_conns[self.get_node_from_index(xi)]:
                        print(self.__node_conns[self.get_node_from_index(xi)][self.get_node_from_index(yi)].getFlux(),
                              end=" ")
                    else:
                        print(-1, end=' ')
            print("")
        print("")

    def list_grau_vertice(self):
        """Lista de graus dos Nodes"""
        lista = {}
        for node in self.__nodes:
            try:
                lista[self.grau_vertice(node)]+=1
            except Exception as _:
                lista[self.grau_vertice(node)]=1
        return lista
    
    def list_grau_conexoes(self):
        """
        estrutura: {
            grau do node:[ {grau  dos conectados: quantos conectados} , vezes identicas]
        }"""
        lista = {}
        for node in self.__nodes:
            graunode = self.grau_vertice(node)
            for _,dest in self.__connections[node].items():
                graudest = self.grau_vertice(dest)
                try:
                    lista[(graunode,graudest)]+=1
                except Exception as _:
                    lista[(graunode,graudest)]=1
        return lista


def complemento(grafo):
    """Inverter as ocorrências de arestas do grafo"""
    leng = len(grafo.matrix)
    matr = [[(1 if grafo.matrix[x][y] < 1 and x != y else 0) for y in range(leng)] for x in range(leng)]
    grp = Graph('complemento_' + grafo.name, grafo.get_direct())
    grp.matrix = matr
    for n in grafo.__nodes:
        grp.__nodes.append(n)
        grp.__visited_node[n] = False
        grp.__connections[n] = {}
    lenn = len(matr)
    lenp = min(1, lenn)
    for xi in range(lenn):
        for yi in range(lenp):
            if xi != yi:
                for am in range(grp.matrix[xi][yi]):
                    grp.__add_edge_man(grp.__nodes[xi], grp.__nodes[yi], xi, yi)
        lenp += 1
    return grp



def print_subgrafos(subgr_list):
    for x1, nl in enumerate(subgr_list):
        print(str((x1 + 1)) + "° conjunto:")
        for nd in nl:
            print(nd.name, end=" ")
        print("")
    print("")

def print_saltos(lista_saltos):
    for direcao_salto in lista_saltos:
        print(direcao_salto[0].name, end=" ")

        while direcao_salto[1] != None:
            direcao_salto = direcao_salto[1]
            print(direcao_salto[0].name, end=" ")
        print()

def ciclico(lista_ciclos):
    if len(lista_ciclos) > 0:
        return True
    return False

def print_ciclos(lista_ciclos):
    for nd_list in lista_ciclos:
        for nd in nd_list:
            if nd == True:
                print("Done")
                continue
            print("Node:", nd.name, end="  ")
        print("")

def sub_grafo(grafo=Graph(),sub_grafo=Graph()):
    for i in sub_grafo.get_nodes():
        if grafo.get_node_by_name(i.name) == None:
            return False # Grafo não contém node do subgrafo
        for _,dest in grafo.get_connections(i).items():
            if grafo.get_node_by_name(dest.name) == None:
                break 
                # Subgrafo tem aresta pra um node
                # que não tá no Grafo
    return True

def isomorfo(grafo1,grafo2):
    if grafo1.get_node_count() != grafo2.get_node_count():
        return False
    if grafo1.get_edge_count() != grafo2.get_edge_count():
        return False
    if grafo1.list_grau_vertice() != grafo2.list_grau_vertice():
        return False
    gr1 = grafo1.list_grau_conexoes()
    gr2 = grafo2.list_grau_conexoes()
    try:
        for pair,data in gr1.items():
            if data != gr2[pair]:
                return False
    except Exception as _:
        return False
    return True
    