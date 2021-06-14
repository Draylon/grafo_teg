import tkinter as tk
from Graph import Graph
root= tk.Tk()

graph = Graph("Grafo",True)

canvas1 = tk.Canvas(root, width = 500, height = 400)
canvas1.pack()


def getOld ():
    entry1 = tk.Entry (root) 
    canvas1.create_window(200, 140, window=entry1)
    x1 = entry1.get()
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)

def getNode ():  
    x1 = entry1.get()
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)

def getEdge ():  
    x1 = entry1.get()
    label1 = tk.Label(root, text= float(x1)**0.5)
    canvas1.create_window(200, 230, window=label1)
    
nodeAdd = tk.Button(text='Adicionar Vertice', command=getNode)
edgeAdd = tk.Button(text='Adicionar Aresta', command=getEdge)
canvas1.create_window(60, 20, window=nodeAdd)
canvas1.create_window(60, 60, window=edgeAdd)

root.mainloop()
