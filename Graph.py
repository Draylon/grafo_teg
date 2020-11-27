
from Node import Node
from Edge import Edge

class Graph:
    def __init__(self,name=None,direcionado=False):
        if name:
            self.name = name
        else:
            self.name = "Graph"
        self.__direcionado=direcionado
        self.__nodes=[]
        self.__edges={}
        self.__connections={}
        self.__visited_node={}
        self.__visited_edge={}

        #== criando matriz
        #self.__matrix = [[0 for y in range(self.numVerticesMaximo)] for x in range(self.numVerticesMaximo)]
        self.matrix = []

    def get_direct(self):
        return self.__direcionado

    def add_node(self,name=None): # add into graph
        n = Node(self,name)
        self.__nodes.append(n)
        print("adding",n.name,"to graph")

        self.__new_to_matrix()
        self.__visited_node[n]=False
        self.__connections[n]={}
        return n

    def remove_node(self,node): # remove from graph
        try:
            if self.__edges == {} or self.__nodes == []:
                return
            print("removing",node.name,"from",self.name)
            ind=self.__nodes.index(node)
            self.disconnect_node(node)
            self.__remove_from_matrix(ind)
            self.__nodes.pop(ind)
            self.__visited_node.pop(node)
            self.__connections.pop(node)
            
        except Exception as exp:
            print("error removing node",exp)

    def disconnect_node(self,node): # delete all edges
        ind=self.__nodes.index(node)
        print("disconnecting node",node.name)
        for edge,_ in self.__visited_node[node].items():
            del edge
        self.__zero_matrix_at(ind)
        for ed,dstn in self.__connections[node].items():
            if dstn == node:
                self.remove_edge(ed)
        
         

    def __zero_matrix_at(self,index):
        ic=0
        while ic < index:
            self.matrix[ic][index]-=1
            ic+=1
        ic+=1
        while ic < len(self.matrix):
            self.matrix[ic][index]-=1
            ic+=1
        self.matrix[index] = [0 for n in range(len(self.__nodes))]

    def __remove_from_matrix(self,index):
        ic=0
        while ic < index:
            self.matrix[ic].pop(index)
            ic+=1
        ic+=1
        while ic < len(self.matrix):
            self.matrix[ic].pop(index)
            ic+=1
        self.matrix.pop(index)
        
    def __new_to_matrix(self):
        r=len(self.matrix)
        for n in range(r):
            self.matrix[n].append(0)
        self.matrix.append([0 for tt in range(r+1)])

    def __update_to_matrix(self,i,j,val):
        self.matrix[i][j]+=val
        if self.__direcionado == False and i != j: self.matrix[j][i]+=val
    
    
    
    #  ==================================



    def add_edge(self,node1,node2,name=None):
        if node1 not in self.__nodes or node2 not in self.__nodes:
            return None
        l1=self.__nodes.index(node1)
        l2=self.__nodes.index(node2)
        e = Edge(self,1,name,self.__direcionado)
        self.__update_to_matrix(l1,l2,1)
        
        self.__connections[node1][e]=node2
        self.__edges[e]=node1
        if self.__direcionado == False and node1 != node2:
            self.__connections[node2][e]=node1

        self.__visited_edge[e]=False
        return e
    
    def __add_edge_man(self,node1,node2,xi,yi,name=None):
        e = Edge(self,1,name,self.__direcionado)
        self.__connections[node1][e]=node2
        self.__edges[e]=node1
        if self.__direcionado == False and xi != yi:
            self.__connections[node2][e]=node1
        self.__visited_edge[e]=False
        return e


    def remove_edge(self,edge):
        print("removing",edge.name,"from",self.name)
        try:
            if self.__edges == {} or self.__nodes == []:
                return
            from_ = self.__edges[edge]
            to_ = self.__connections[from_][edge]
            self.__connections[from_].pop(edge)
            self.__connections[to_].pop(edge)
            self.__visited_edge.pop(edge)
            self.__edges.pop(edge)
        except Exception as exp:
            print("error removing edge",edge.name,"\nerr:",exp)



    #  ==================================



    def __pathing_list(self,current,arrival,edge_list=[]):
        for edge,dest_ in self.__connections[current].items():
            if self.__visited_edge[edge] == False:
                edge_list.append(edge)
                self.__visited_edge[edge]=True
                if dest_ == arrival:
                    self.__pathing_list.append(edge_list)
                    break
                else:
                    self.__pathing_list(dest,arrival,edge_list)
    

    def max_weight(self,departure,arrival):
        if departure not in self.__nodes or arrival not in self.__nodes:
            return -1
        self.__pathing_list=[]
        self.__pathing_list(departure,arrival)
        self.__clear_visited_edges()
        shortest_path=-1
        for path in self.__pathing_list:
            path_weight=0
            for edge in path:
                path_weight = path_weight+edge.weight
            if path_weight < shortest_path or shortest_path == -1:
                shortest_path = path_weight
        del self.__pathing_list

    # percorrer partida até chegada, procurando o menor caminho
    def min_weight(self,departure,arrival):
        if departure not in self.__nodes or arrival not in self.__nodes:
            return -1
        self.__pathing_list=[]
        self.__pathing_list(departure,arrival)
        shortest_path=-1
        for path in self.__pathing_list:
            path_weight=0
            for edge in path:
                path_weight = path_weight+edge.weight
            if path_weight < shortest_path or shortest_path == -1:
                shortest_path = path_weight
        del self.__pathing_list



    #  ================================

    def __clear_visited_nodes(self):
        for n in self.__visited_node.keys():
            self.__visited_node[n]=False
    def __clear_visited_edges(self):
        for e in self.__visited_edges.keys():
            self.__visited_edges[e]=False
    


    def most_connected(self):
        most_ = []
        ammo,xn = -1,0
        for xi,x in enumerate(self.matrix):
            new_ammo=0
            for yi,y in enumerate(x):
                new_ammo+= 2*y if xi==yi else y
            if new_ammo == ammo:
                most_.append(xn)
            if new_ammo > ammo or ammo==-1:
                most_=[xn]
                ammo=new_ammo

            xn+=1
        return most_,ammo

    def least_connected(self):
        most_ = []
        ammo,xn = -1,0
        for xi,x in enumerate(self.matrix):
            new_ammo=0
            for yi,y in enumerate(x):
                new_ammo+= 2*y if xi==yi else y
            if new_ammo == ammo:
                most_.append(xn)
            if new_ammo < ammo or ammo==-1:
                most_=[xn]
                ammo=new_ammo

            xn+=1
        return most_,ammo


    def next_node(self,node,edge):
        try:
           return self.connections[node][edge]
        except expression as identifier:
            return None
    

    def print_subgrafos(self,sg_list):
        for x1,nl in enumerate(sg_list):
            print(str((x1+1))+"° conjunto:")
            for nd in nl:
                print(nd.name,end=" ")
            print("")
        print("")

    def sub_grafos(self):
        self.__sub_grafl=[[]]
        nc=0
        for node in self.__nodes:
            if self.__visited_node[node] == False:
                self.__sub_grafos_rec(nc,node)
                nc+=1
                self.__sub_grafl.append([])
        self.__sub_grafl.pop()
        self.__clear_visited_nodes()
        return self.__sub_grafl.copy()

    def __sub_grafos_rec(self,curr,node):
        if self.__visited_node[node] == False:
            self.__sub_grafl[curr].append(node)
            self.__visited_node[node] = True
            for edge,dest_ in self.__connections[node].items():
                self.__sub_grafos_rec(curr,dest_)
        return

    '''
========================================================
========================================================
========================================================
    '''
    

    def print(self):
        for node in self.__nodes:
            print("Node",node.name,"\n    conectado a: ",end="")
            try:
                nn=True
                for edge,dest1 in self.__connections[node].items():
                    nn=False
                    print("("+edge.name+","+dest1.name+")",end=" ")
                if nn == True: print("Nenhum",end="")
                print("\n")
            except Exception as ex:
                print("Erro",ex,"\n")
        print("")

    def print_matriz(self):
        print("Matriz:")
        for x in self.matrix:
            for y in x:
                print(y,end=" ")
            print("")
        print("")

    def __del__(self):
        self.__nodes.clear()
        self.__edges.clear()
        self.__connections.clear()
        self.__visited_edge.clear()
        self.__visited_node.clear()
        print("Graph",self.name,"Deleted!")



    '''
========================================================
========================================================
========================================================
    '''
    def complemento(grafo):
        matr=[ [ (0 if grafo.matrix[x][y] >= 1 else 1) for y in range(len(grafo.matrix[0]))]  for x in range(len(grafo.matrix)) ]
        grp=Graph('complemento_'+grafo.name,grafo.get_direct())
        grp.matrix=matr
        for n in grafo.__nodes:
            grp.__nodes.append(n)
            grp.__visited_node[n]=False
            grp.__connections[n]={}
        lenn = len(matr)
        lenp=min(1,lenn)
        for xi in range(lenn):
            for yi in range(lenp):
                for am in range(grp.matrix[xi][yi]):
                    grp.__add_edge_man(grp.__nodes[xi],grp.__nodes[yi],xi,yi)
            lenp+=1
        return grp

    def conexo(self):
        subg = self.sub_grafos()
        legc=len(subg)
        if legc == 1:
            print("Grafo conexo, com",legc,"subconjunto")
            return True,legc
        print("Grafo disconexo, com",legc,"subconjuntos")
        return False,legc


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
    '''