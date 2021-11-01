import networkx as nx
import matplotlib.pyplot as plt
import random

print("hi, this is program 3")


# empty undirected graph
G= nx.Graph()

#add nodes
G.add_node(0)
G.add_nodes_from( [1,2,3])


#add edges
G.add_edge(0,1)
G.add_edges_from( [ (1,2), (2,3), (3,1) ] )

print(" Number of nodes=", G.number_of_nodes())
print(" Number of edges=", G.number_of_edges())

print("G.nodes :", G.nodes)
print("G.edges :", G.edges)
print("G.degree:", G.degree)
print("G.adj :", G.adj)

#for key in G:
#    print("key : {} , Value : {}".format(key,G[key]))
print(" bye ")

