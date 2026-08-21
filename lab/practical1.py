import networkx as nx
import random as rd
import matplotlib.pyplot as plt

g = nx.Graph()

no_of_nodes = rd.randint(8, 26)

max_edges = no_of_nodes * (no_of_nodes - 1) // 2

for i in range(no_of_nodes):
    g.add_node(chr(65 + i))

for i in range(1, no_of_nodes):
    g.add_edge(chr(65 + i - 1), chr(65 + i))

total_edges = rd.randint(no_of_nodes - 1, max_edges)
remaining_edges = total_edges - (no_of_nodes - 1)

for i in range(remaining_edges):
    u = chr(65 + rd.randint(0, no_of_nodes - 1))
    v = chr(65 + rd.randint(0, no_of_nodes - 1))

    if u != v:
        g.add_edge(u, v)



print("No. of Nodes in the graph:", g.number_of_nodes())
print("No. of Edges in the graph:", g.number_of_edges())

print("\nDegree of each node:")
for node, degree in g.degree():
    print(node, ":", degree)


node_colors = []
font_colors = []

for node in g.nodes():
    index = ord(node) - 65

    if index % 2 == 0:
        node_colors.append("red")
    else:
        node_colors.append("blue")

    font_colors.append("white")

nx.draw(
    g,
    with_labels=True,
    node_color=node_colors,
    node_size=800,
    edge_color="black",
    font_color="white"
)

plt.show()


