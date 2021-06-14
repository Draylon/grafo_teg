from Graph import Graph
from networkx_adapter import *

"""

MAPA DO BAIRRO BUCAREIN

"""

grafo = Graph("Bairro Bucarein",True) # Direcionado 
#pos = {0: (0, 1), 1: (1, 1), 2: (2,0), 3: (2, 2),4:(3,1),5:(4,1),6:(5,1)}


#  ┌─────────────────────┐
#  │ Pontos de interesse │
#  └─────────────────────┘

"""n1 = grafo.add_node("Giassi")
n2 = grafo.add_node("Valgri")
n3 = grafo.add_node("Santander")
n4 = grafo.add_node("Itau")
n5 = grafo.add_node("Fort Atacadista")
n6 = grafo.add_node("Correios")
n7 = grafo.add_node("Arena Grill")
n8 = grafo.add_node("Arena Joinville")
n9 = grafo.add_node("Havan")
n11 = grafo.add_node("Celso Ramos")
n12 = grafo.add_node("São José")
n13 = grafo.add_node("Adriano Lanches")
n14 = grafo.add_node("Tokio Eletronica")
n15 = grafo.add_node("Shopping Big")
n15 = grafo.add_node("Posto Ipiranga")
n16 = grafo.add_node("Senai Sul")
n17 = grafo.add_node("Pizzaria QMassa")
n18 = grafo.add_node("Laboratorio Gimenes")
n19 = grafo.add_node("Doceria São josé")"""

#  ┌─────────────┐
#  │ Cruzamentos │
#  └─────────────┘

cruzamentos = 38 # número de cruzamentos colocados
cl = [ grafo.add_node("c"+str(i)) for i in range(cruzamentos)]


# Horizontais
grafo.add_edge(cl[0],cl[1],capacidade=241,add_parallel=True)
grafo.add_edge(cl[2],cl[36],capacidade=267)
grafo.add_edge(cl[3],cl[4],capacidade=263)
grafo.add_edge(cl[4],cl[5],capacidade=210)
grafo.add_edge(cl[5],cl[6],capacidade=292,add_parallel=True)
grafo.add_edge(cl[6],cl[7],capacidade=223,add_parallel=True)
grafo.add_edge(cl[8],cl[9],capacidade=270)
grafo.add_edge(cl[9],cl[10],capacidade=204,add_parallel=True)
grafo.add_edge(cl[11],cl[12],capacidade=263,add_parallel=True)
grafo.add_edge(cl[12],cl[13],capacidade=198,add_parallel=True)
grafo.add_edge(cl[13],cl[14],capacidade=510,add_parallel=True)
grafo.add_edge(cl[14],cl[37],capacidade=510,add_parallel=True)
grafo.add_edge(cl[16],cl[15],capacidade=240)
grafo.add_edge(cl[17],cl[16],capacidade=250)
grafo.add_edge(cl[18],cl[17],capacidade=211)
grafo.add_edge(cl[19],cl[18],capacidade=295)
grafo.add_edge(cl[20],cl[19],capacidade=216)
grafo.add_edge(cl[21],cl[20],capacidade=282)
grafo.add_edge(cl[22],cl[23],capacidade=230)
grafo.add_edge(cl[23],cl[24],capacidade=230)
grafo.add_edge(cl[24],cl[25],capacidade=207)
grafo.add_edge(cl[25],cl[26],capacidade=520)
grafo.add_edge(cl[26],cl[27],capacidade=286)
grafo.add_edge(cl[29],cl[30],capacidade=220)
grafo.add_edge(cl[30],cl[31],capacidade=266)
grafo.add_edge(cl[31],cl[32],capacidade=216)
grafo.add_edge(cl[34],cl[33],capacidade=269)
grafo.add_edge(cl[35],cl[34],capacidade=228,add_parallel=True)

# Verticais
grafo.add_edge(cl[15],cl[22],capacidade=192)
grafo.add_edge(cl[22],cl[28],capacidade=169)
grafo.add_edge(cl[28],cl[29],capacidade=114)

grafo.add_edge(cl[0],cl[2],capacidade=161)
grafo.add_edge(cl[2],cl[3],capacidade=106)
grafo.add_edge(cl[3],cl[8],capacidade=106)
grafo.add_edge(cl[8],cl[11],capacidade=94)
grafo.add_edge(cl[11],cl[16],capacidade=190)
grafo.add_edge(cl[16],cl[23],capacidade=193)
grafo.add_edge(cl[23],cl[30],capacidade=290,add_parallel=True)
grafo.add_edge(cl[30],cl[33],capacidade=217,add_parallel=True)

grafo.add_edge(cl[36],cl[1],capacidade=241)
grafo.add_edge(cl[4],cl[36],capacidade=98)
grafo.add_edge(cl[9],cl[4],capacidade=91)
grafo.add_edge(cl[12],cl[9],capacidade=82)
grafo.add_edge(cl[17],cl[12],capacidade=203)
grafo.add_edge(cl[24],cl[17],capacidade=191)
grafo.add_edge(cl[31],cl[24],capacidade=284)
grafo.add_edge(cl[34],cl[31],capacidade=209)

grafo.add_edge(cl[35],cl[32],capacidade=213)
grafo.add_edge(cl[32],cl[25],capacidade=289)
grafo.add_edge(cl[25],cl[18],capacidade=187)
grafo.add_edge(cl[18],cl[13],capacidade=184)
grafo.add_edge(cl[13],cl[10],capacidade=86)
grafo.add_edge(cl[10],cl[5],capacidade=100)

grafo.add_edge(cl[6],cl[19],capacidade=375,add_parallel=True)

grafo.add_edge(cl[14],cl[7],capacidade=183)
grafo.add_edge(cl[20],cl[14],capacidade=182)
grafo.add_edge(cl[20],cl[26],capacidade=179)

grafo.add_edge(cl[21],cl[37],capacidade=213)
grafo.add_edge(cl[27],cl[21],capacidade=175)

# Diagonal

grafo.add_edge(cl[7],cl[37],capacidade=302)

#  ┌──────────────────────┐
#  │ Grau dos cruzamentos │
#  └──────────────────────┘

mcon = grafo.most_connected()
lcon = grafo.least_connected()
print("mais conectados:",mcon[0],"Grau:",mcon[1])
print("menos conectados:",lcon[0],"Grau:",lcon[1])

#  ╔═══════════════════╗
#  ║┌─────────────────┐║
#  ║│ Desenho do mapa │║
#  ║└─────────────────┘║
#  ╚═══════════════════╝

#posições parecidas com a do mapa real
pos = {0:(1,10),1:(2,10),2:(1,9),36:(2,9),3:(1,8),4:(2,8),5:(3,8),6:(4,8),7:(5,8),8:(1,7),9:(2,7),10:(3,7),11:(1,6),12:(2,6),13:(3,6),14:(5,6),37:(6,6),15:(0,5),16:(1,5),17:(2,5),18:(3,5),19:(4,5),20:(5,5),21:(7,5),22:(0,3),23:(1,3),24:(2,3),25:(3,3),26:(5,3),27:(6,3),28:(0,2),29:(0,1),30:(1,1),31:(2,1),32:(3,1),33:(1,0),34:(2,0),35:(3,0)}
nxg = create_networkx_graph(grafo)
#networkx_draw(nxg,grafo.get_node_connections())
networkx_draw(nxg,grafo.get_node_connections(),pos,True)
