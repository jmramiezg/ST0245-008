import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#O(n)
A = np.matrix([[1,1], [2,1]])
G = nx.from_numpy_matrix(A)
nx.draw(G)
plt.show()

G1 = nx.Graph()
G1.add_node(1)
G1.add_node(2)
G1.add_nodes_from([3,4,5])
G1.add_edge(1,2)
G1.add_edge(1,3)
G1.add_edges_from([(2,3), (2,4)])
G1.add_edges_from([(4,3), (4,5)])
print(G1.nodes)
print(G1.edges)

'''
La complejidad algoritmica de este grafo, es O(n), ya que su complejidad depende de la cantidad de elementos que queramos añadir
a este grafo, si deseamos añadir 20 nodos, el algoritmo debera hacer una asignacion para cada uno de estos nododos nuevos, al igual
que para los arcos que conectan a estos.
'''

