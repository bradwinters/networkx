import networkx as nx
import matplotlib.pyplot as plt

print("hi")

G= nx.Graph()
G.add_edge('A','B', weight=13, relation='freind')
G.add_edge('B','C', weight=9, relation='family')
G.add_edge('B','D', weight=7, relation='freind')
G.add_edge('E','B', weight=10, relation='freind')
G.add_edge('E','A', weight=1, relation='enemy')
G.add_edge('F','B', weight=13, relation='family')
G.edges(data=True)

print("try to print the newtwork so far")
print(G)
# display what class g can do
# print(help(G))
for key in G:
    print("key : {} , Value : {}".format(key,G[key]))
print(" bye ")

