import networkx as nx
from matplotlib import pyplot as plt
import time

G = nx.read_edgelist("Integer Graphs Sampled/newIntGraph2012.csv", delimiter=',', nodetype=int)

# Get a node that has about 100 edges.
nodes = nx.nodes(G)
G2 = nx.Graph()
for node in nodes:
    edges = G.edges(node)
    if 30 < len(edges) < 100:
        for edge in edges:
            G2.add_edge(edge[0], edge[1])
        break

k = G2.subgraph(G2.nodes())
plt.figure()
plt.axis('off')
nx.draw_networkx(k, with_labels=False)
plt.savefig('hub')

# Get a bunch of nodes with only 2 connections
G3 = nx.Graph()
counter = 30
for node in nodes:
    edges = G.edges(node)
    if len(edges) == 1:
        for edge in edges:
            G3.add_edge(edge[0], edge[1])
        counter -= 1
    if counter == 0:
        break

k = G3.subgraph(G3.nodes())
plt.figure()
plt.axis('off')
nx.draw_networkx(k, with_labels=False, width=20)
plt.savefig('regular.png')
