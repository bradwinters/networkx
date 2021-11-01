import networkx as nx
import matplotlib.pyplot as plt
import random

print("hi, this is program 3")


# empty undirected graph
G= nx.Graph()

#add nodes
G.add_node(0)
G.add_nodes_from( [1,2,3]}


#add edges
G.add_edge('A','B', weight=13, relation='freind')
G.add_edge('B','C', weight=9, relation='family')

print(" Number of nodes=", G.number_of_nodes())
print(" Number of edges=", G.number_of_edges())




#for key in G:
#    print("key : {} , Value : {}".format(key,G[key]))
print(" bye ")

