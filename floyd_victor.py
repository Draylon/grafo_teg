# INF representa o vertice no qual nao se liga a outro vertice,
# definindo um valor muito acima dos demais na hora de
# realizar o min entre os vertices este será ignorado.


INF = 99999

grafo = [
    [0, 3, INF, 5],
    [2, 0, INF, 4],
    [INF, 1, 0, INF],
    [INF, INF, 2, 0]
]

# Numero de vertices no GRAFO
V = len(grafo)

def floydWarshall(graph):
    dist = graph.copy()
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    printSolution(dist, "Matriz com o caminho minimo entre cada vertice")


def printSolution(dist, msg=""):
    print(msg)
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                print("%7s" % "INF", end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end="")
            if j == V - 1:
                print("")


printSolution(grafo, "Matriz original")
print("+++++++++++++++++++++++++++++++============+++++++++++++++++")
floydWarshall(grafo)
