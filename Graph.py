from Node import Node
from Edge import Edge
from queue import MQueue
import decimal
from networkx_adapter import *

INF = float("inf")
# noinspection SpellCheckingInspection
class Graph:
    def __init__(self, name=None, direcionado=False):
        if name:
            self.name = name
        else:
            self.name = "Graph"
        self.__direcionado = direcionado
        self.__nodes = []
        self.__edges = {}
        self.__connections = {}
        self.__node_conns = {}
        self.__visited_node = {}
        self.__visited_edge = {}

        # == criando matriz
        # self.__matrix = [[0 for y in range(self.numVerticesMaximo)] for x in range(self.numVerticesMaximo)]
        self.matrix = []

    def is_directed(self):
        return self.__direcionado

    def add_node(self, name=None,position=()):  # add into graph
        n = Node(self, name,position=position)
        self.__nodes.append(n)
        # print("adding",n.name,"to graph")

        self.__new_to_matrix()
        self.__visited_node[n] = False
        self.__connections[n] = {}
        self.__node_conns[n] = {}
        return n

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

        except Exception as exp:
            pass
            # print("error removing node",exp)

    def disconnect_node(self, node):  # delete all edges
        ind = self.__nodes.index(node)
        for edge, _ in self.__visited_node[node].items():
            del edge
        self.__zero_matrix_at(ind)
        for ed, dstn in self.__connections[node].items():
            if dstn == node:
                self.remove_edge(ed)

    def get_index_from_node(self, node):
        return self.__nodes.index(node)

    def get_node_from_index(self, index):
        return self.__nodes[index]

    def get_node_dictionary(self):
        dicct = {}
        for i,e in enumerate(self.__nodes):
            dicct[i]=e
        return dicct

    def get_nodes(self):return self.__nodes

    def get_edges(self): return self.__edges

    def get_edge(self, node1, node2):
        if self.__direcionado is True:
            return self.__node_conns[node1][node2]
        else:
            try:
                return self.__node_conns[node1][node2]
            except KeyError as kr:
                try:
                    return self.__node_conns[node2][node1]
                except KeyError as kr2:
                    return None

    def get_nodes_from_edge(self,edge):
        for from_,data_ in self.__node_conns.items():
            for dest_,edge_ in data_.items():
                if edge_ == edge:
                    return from_,dest_
        return None,None

    def get_connections(self, node):
        return self.__connections[node]

    def get_node_connections(self):return self.__node_conns

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

    def __new_to_matrix(self):
        r = len(self.matrix)
        for n in range(r):
            self.matrix[n].append(0)
        self.matrix.append([0 for tt in range(r + 1)])

    def __update_to_matrix(self, i, j, val):
        self.matrix[i][j] += val
        if self.__direcionado is False and i != j: self.matrix[j][i] += val

    def next_node(self, node, edge):
        try:
            return self.connections[node][edge]
        except Exception as identifier:
            return None

    '''
========================================================
========================================================
========================================================
    '''

    def add_edge(self, node1, node2, name=None,capacidade=0,fluxo=0):
        if node1 not in self.__nodes or node2 not in self.__nodes:
            return None
        l1 = self.__nodes.index(node1)
        l2 = self.__nodes.index(node2)
        e = Edge(self, 1, name, self.__direcionado,capacidade,fluxo)
        self.__update_to_matrix(l1, l2, 1)

        self.__connections[node1][e] = node2
        self.__node_conns[node1][node2]=e
        self.__edges[e] = node1
        if self.__direcionado == False and node1 != node2:
            self.__connections[node2][e] = node1
            self.__node_conns[node2][node1]=e

        self.__visited_edge[e] = False
        return e

    def __add_edge_man(self, node1, node2, xi, yi, name=None):
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

    '''
    ========================================================
    ========================================================
    ========================================================
        '''

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

    '''
========================================================
========================================================
========================================================
    '''

    def grau_vertice(self, index):
        grau = 0
        for xi, x in enumerate(self.matrix[index]):
            grau += 2 * x if xi == index else x
        return grau

    def grau_vertices(self):
        print("Grau dos vertices")
        for n in range(len(self.__nodes)):
            print("Node", self.__nodes[n].name, " grau:", self.grau_vertice(n))

    '''
========================================================
========================================================
========================================================
    '''

    def __pathing_rec(self, current, arrival,allow_visited_edges=False,allow_visited_nodes=False,allow_return_edge=False, edge_list=[None],depth=0):
        for edge, dest_ in self.__connections[current].items():
            if not allow_return_edge and edge.getFlux() < 0:
                return
            if self.__visited_edge[edge] == True and not allow_visited_edges:
                return
            if self.__visited_node[current] == True and not allow_visited_nodes:
                return
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
                self.__pathing_rec(dest_, arrival,allow_visited_edges,allow_visited_nodes,allow_return_edge,edge_list,depth+1)

    def max_weight(self, departure, arrival):
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
                shortest_path = path_weight
        del self.__pathing_list
        return longest_path

    # percorrer partida até chegada, procurando o menor caminho
    def min_weight(self, departure, arrival):
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

    '''
    ========================================================
    ========================================================
    ========================================================
        '''

    def __clear_visited_nodes(self):
        for n in self.__visited_node.keys():
            self.__visited_node[n] = False

    def __clear_visited_edges(self):
        for e in self.__visited_edge.keys():
            self.__visited_edge[e] = False

    def most_connected(self):
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
        ind_l, ammo = self.most_connected()
        nodes = []
        for ind in ind_l:
            nodes.append(self.get_node_from_index(ind))
        return nodes, ammo

    def least_connected_objects(self):
        ind_l, ammo = self.least_connected()
        nodes = []
        for ind in ind_l:
            nodes.append(self.get_node_from_index(ind))
        return nodes, ammo

    def print_subgrafos(self, sg_list):
        for x1, nl in enumerate(sg_list):
            print(str((x1 + 1)) + "° conjunto:")
            for nd in nl:
                print(nd.name, end=" ")
            print("")
        print("")

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
            for edge, dest_ in self.__connections[node].items():
                self.__sub_grafos_rec(curr, dest_)
        return

    def print_pontes(set_):
        for ed in set_:
            print(ed.name, end=" ")
        print()

    def pontes(self, lista_ciclos):
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

    def arvore(self, lista_ciclos):
        if (not Graph.ciclico(lista_ciclos) and self.conexo()[0] == True):
            return True
        else:
            return False

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

    def __ciclo_def(self, ind, curr, targ, from_ed):
        # print("Current:",ind,"targ:",targ.name,end=" | ")

        for ed, dest in self.__connections[curr].items():
            if ed not in from_ed and self.__visited_edge[ed] == True:
                from_ed.append(ed)
                # print("node:",curr.name,"edge:",ed.name,"dest:",dest.name)
                try:
                    try:
                        indnode = self.__cycle_list[ind].index(curr)
                        # print(curr.name,"already exists")
                        self.__cycle_list[ind] = self.__cycle_list[ind][:(indnode + 1)]
                    except Exception as exde:
                        # print("err",curr.name,"not found")
                        # print("adding",curr.name,"to list\n")
                        self.__cycle_list[ind] += [curr]
                    if dest == targ:
                        # print("Found=====\n")
                        self.__cycle_list[ind] += [dest]
                        # print("added-found",dest.name,self.__cycle_list[ind][-1].name)
                except ValueError as exc:
                    # print("err",curr.name,"not found")
                    # print("adding",curr.name,"to list\n")
                    self.__cycle_list[ind] += [curr]
                except Exception as exc:
                    print(exc)

                if dest == targ:
                    return True
                self.__visited_edge[ed] = False
                if self.__ciclo_def(ind, dest, targ, from_ed) == True:
                    return True
                '''try:
                    rind=from_ed.index(ed)
                    if (len(from_ed)-1-rind) != 0 and self.__cycle_list[ind][len(self.__cycle_list[ind])-1][1] != 2:
                        #print("removing",rind)
                        self.__cycle_list[ind][rind][1]=0
                        self.__cycle_list[ind][rind+1][1]=0
                except Exception as identifier:
                    pass'''

        # self.__cycle_list[ind]+=[(curr,0)]

    def __ciclos_rec(self):
        node = self.__node_queue.pop()
        if node:
            ##print("popped",node.name)
            for ed, dest in self.__connections[node].items():
                if self.__visited_edge[ed] == False:
                    # print("going to",dest.name,"with",ed.name)
                    if self.__node_queue.has(dest):
                        # print(dest.name,"already exists in queue")
                        self.__visited_edge[ed] = True
                        # print("\ndetecting cycle\n")
                        self.__cycle_list.append([])
                        self.__ciclo_def(len(self.__cycle_list) - 1, node, dest, [ed])
                        # print("\ncycle done\n")
                        for li in self.__cycle_list[-1]:
                            if li == True:
                                # print("Done")
                                continue
                            # print(li.name,end=" | ")
                        # print("//")
                        if len(self.__cycle_list[-1]) < 3:
                            self.__cycle_list.pop()
                            break
                    else:
                        # print("adding",dest.name)
                        self.__node_queue.push(dest)
                        self.__visited_edge[ed] = True
            return self.__ciclos_rec()
        return

    def ciclos(self):
        self.__node_queue = MQueue()
        self.__cycle_list = []
        if len(self.__nodes) > 0:
            self.__node_queue.push(self.__nodes[0])
            self.__ciclos_rec()

        self.__clear_visited_edges()
        return self.__cycle_list.copy()

    '''
========================================================
========================================================
========================================================
    '''

    def print(self):
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

    def __del__(self):
        self.__nodes.clear()
        self.__edges.clear()
        self.__connections.clear()
        self.__node_conns.clear()
        self.__visited_edge.clear()
        self.__visited_node.clear()
        # print("Graph",self.name,"Deleted!")

    '''
========================================================
========================================================
========================================================
    '''

    def complemento(grafo):
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

    def print_saltos(lista_saltos):
        for direcao_salto in lista_saltos:
            print(direcao_salto[0].name, end=" ")

            while direcao_salto[1] != None:
                direcao_salto = direcao_salto[1]
                print(direcao_salto[0].name, end=" ")
            print()

    '''
    ========================================================
    ========================================================
    ========================================================
    '''

    def __dfs_rec(self,init,last=None,iter=0):
        if self.__visited_node[init] < iter and self.__visited_node[init] is not False:
            return
        self.__visited_node[init] = iter
        for edge,destination in self.__connections[init].items():
            if destination != last:
                self.__dfs_rec(destination,init,iter+1)

    def dfs(self, init):
        self.__clear_visited_nodes()
        self.__dfs_rec(init)
        return self.__visited_node.copy()

    def print_dfs(self,list):
        for index, path in enumerate(list):
            print("Caminho", index)
            for node in path:
                print(node, end=" - ")
            print("")

    def dfs_paths(self,departure,arrival):
        if departure not in self.__nodes or arrival not in self.__nodes:
            return -1
        self.__pathing_list = []
        self.__clear_visited_edges()
        self.__pathing_rec(departure, arrival,True)
        cp1 = self.__pathing_list.copy()
        del self.__pathing_list
        return cp1

    def calcular_fluxo(self,node):
        """
        SOMAR OS FLUXOS DO VÉRTICE DE SAÍDA
        """
        fluxo=0
        for edge,destination in self.__connections[node]:
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
        self.__pathing_rec(departure, arrival,False,True)
        len_fluxos = len(self.__pathing_list)
        edges_list = set()
        for edge_l in self.__pathing_list:
            for edge in edge_l:
                if edge.getCap() == edge.getFlux():
                    edges_list.add(edge)

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

    """
    ===============================
    ===============================
    ===============================
    """


    def edmondsKarp(self,s, t):
        n = len(self.__edges)
        flow = 0
        iterb=0
        while True:
            P = [-1 for x in range(n)]
            P[s] = -2
            M = [0 for x in range(n)]
            M[s] = decimal.Decimal('Infinity')
            BFSq = []
            BFSq.append(s)
            pathFlow, P = self.BFSEK(s, t, P, M, BFSq)
            if pathFlow == 0:
                break
            flow = flow + pathFlow
            v = t
            while v != s:
                u = P[v]
                self.__node_conns[u][v].addFlux(pathFlow)
                #self.__node_conns[v][u].addFlux(-1*pathFlow)
                try:
                    self.__node_conns[v][u].addFlux(-1*pathFlow)
                except KeyError as ke:
                    self.add_edge(v,u,capacidade=self.__node_conns[u][v].getCap())
                    self.__node_conns[v][u].setFlux(-1*pathFlow)
                v = u
            iterb+=1
            #nxg = create_networkx_graph(self)
            #networkx_draw(nxg, self.get_node_connections())
        print(iterb,"iterações")
        return flow

    def BFSEK(self,s, t, P, M, BFSq):
        while (len(BFSq) > 0):
            u = BFSq.pop(0)
            for v,e in self.__node_conns[u].items():
                if e.getCap() - e.getFlux() > 0 and P[v] == -1:
                    P[v] = u
                    M[v] = min(M[u], e.getCap() - e.getFlux())
                    if v != t:
                        BFSq.append(v)
                    else:
                        return M[t], P
        return 0, P

    """
    ===================================
    ===================================
    ===================================
    """
    """
    def searching_algo_BFS(self, s, t, parent):
        visited = [False] * len(self.__nodes)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            for desv, edge in self.__node_conns[u].items():
                if visited[desv] == False and edge.getCap() > 0:
                    queue.append(desv)
                    visited[desv] = True
                    parent[desv] = u
        return True if visited[t] else False

    def ford_fulkerson(self, source, sink):
        parent = [-1] * len(self.__nodes)
        max_flow = 0
        iterb=0
        while self.searching_algo_BFS(source, sink, parent):
            path_flow = float("99")
            s = sink
            while (s != source):
                path_flow = min(path_flow, self.__node_conns[self.get_node_from_index(parent[s])][s].getCap() )
                s = parent[s]
            # Adding the path flows
            max_flow += path_flow
            # Updating the residual values of edges
            v = sink
            while (v != source):
                u = parent[v]
                self.__node_conns[u][v].addCap(-1*path_flow)
                self.__node_conns[u][v].setFlux(-1*max_flow)
                try:
                    self.__node_conns[v][u].addCap(path_flow)
                    self.__node_conns[v][u].addFlux(path_flow)
                except KeyError as ke:
                    self.add_edge(v,u)
                    self.__node_conns[v][u].setCap(path_flow)
                    self.__node_conns[v][u].setFlux(path_flow)
                v = parent[v]
            iterb+=1
        print(iterb,"iterações")
        return max_flow
"""

    # This is a sample depth first search to be used at max_flow
    def depth_first_search(self,lvl,ptr,adj, vertex, sink, flow):
        if vertex == sink or not flow:
            return flow

        for i in range(ptr[vertex], len(adj[vertex])):
            e = adj[vertex][i]
            if lvl[e[0]] == lvl[vertex] + 1:
                p = self.depth_first_search(lvl[:],ptr[:],adj[:],e[0], sink, min(flow, e[2] - e[3]))
                if p:
                    adj[vertex][i][3] += p
                    adj[e[0]][e[1]][3] -= p
                    return p
            ptr[vertex] = ptr[vertex] + 1
        return 0

    def dinitz(self, source, sink):
        n = len(self.__nodes)
        lvl = [0] * n
        ptr = [0] * n
        q = [0] * n
        adj = [[] for _ in range(n)]
        flow, q[0] = 0, source
        for l in range(31):
            while True:
                lvl, ptr = [0] * len(q), [0] * len(q)
                qi, qe, lvl[source] = 0, 1, 1
                while qi < qe and not lvl[sink]:
                    v = q[qi]
                    qi += 1
                    for e in adj[v]:
                        if not lvl[e[0]] and (e[2] - e[3]) >> (30 - l):
                            q[qe] = e[0]
                            qe += 1
                            lvl[e[0]] = lvl[v] + 1
                p = self.depth_first_search(lvl,ptr,adj,source, sink, INF)
                while p:
                    flow += p
                    p = self.depth_first_search(lvl,ptr,adj,source, sink, INF)
                if not lvl[sink]:
                    break
        return flow


    '''def most_connected(self):
        conn_number = -1
        r_node = []
        for node,n_ind in self.__nodes:
            if len(node.__edges) > conn_number:
                r_node = [node]
                conn_number=len(node.__edges)
            if len(node.__edges) == conn_number:
                r_node.append(node)
        return r_node,conn_number

    def least_connected(self):
        conn_number = -1
        r_node = []
        for node,n_ind in self.__nodes:
            if len(node.__edges) < conn_number:
                r_node = [node]
                conn_number=len(node.__edges)
            if len(node.__edges) == conn_number:
                r_node.append(node)
        return r_node,conn_number


        print("atual:",curr," ","node:",node.name,end=" ")
        if self.__visited_edge[from_edge] == False:
            self.__visited_edge[from_edge]=True
            print("grau:",self.grau_vertice(n_ind),end="")
            action=''
            if self.grau_vertice(n_ind) > 1:
                if len(self.__node_curr)-1 == curr: #já tem um ciclo em curr
                    if self.grau_vertice(n_ind) == 2:
                        action='update'
                    else:
                        action='new'
                else:
                    action='new'
            else:
                action='update'
            if action == 'new':
                print("\nComecar novo ciclo\n")
                for ed,destt in self.__connections[node].items():
                    if ed != from_edge:
                        in_dst = self.__nodes.index(destt)
                        self.__ciclos_rec(curr+1,destt,in_dst,ed)
            elif action == 'update':
                print("\nContinuar anterior",curr,"\n")
                for ed,destt in self.__connections[node].items():
                    if ed != from_edge:
                        in_dst = self.__nodes.index(destt)
                        self.__ciclos_rec(curr,destt,in_dst,ed)
        
        else: # Encontrou um ciclo
            print("\nEncontrou um ciclo!\n")
            cl_ind = self.__edge_curr[from_edge]
    '''
