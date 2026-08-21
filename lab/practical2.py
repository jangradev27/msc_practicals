import networkx as nx
import random as rd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

g = nx.Graph()

no_of_students = rd.randint(8, 15)

departments = ["CSE", "ECE", "ME"]
interests = ["AI", "Robotics", "Web Development", "Cybersecurity"]

for i in range(no_of_students):

    student = chr(65 + i)

    age = rd.randint(18, 25)

    department = departments[rd.randint(0, 2)]

    interest = interests[rd.randint(0, 3)]

    g.add_node(
        student,
        age=age,
        department=department,
        interest=interest
    )


max_edges = no_of_students * (no_of_students - 1) // 2

total_edges = rd.randint(no_of_students - 1, max_edges)


for i in range(1, no_of_students):

    u = chr(65 + i - 1)
    v = chr(65 + i)

    g.add_edge(u, v)


while g.number_of_edges() < total_edges:

    u = chr(65 + rd.randint(0, no_of_students - 1))
    v = chr(65 + rd.randint(0, no_of_students - 1))

    if u != v:
        g.add_edge(u, v)


department_colors = {
    "CSE": "yellow",
    "ECE": "orange",
    "ME": "brown"
}


node_colors = []

for node in g.nodes():

    department = g.nodes[node]["department"]

    node_colors.append(department_colors[department])


node_sizes = []

for node in g.nodes():

    age = g.nodes[node]["age"]

    node_sizes.append(age * 50)


node_labels = {}

for node in g.nodes():

    node_labels[node] = g.nodes[node]["age"]


nx.draw(
    g,
    labels=node_labels,
    node_color=node_colors,
    node_size=node_sizes,
    edge_color="gray",
    font_color="black"
)


legend_elements = [
    Patch(facecolor="yellow", label="CSE"),
    Patch(facecolor="orange", label="ECE"),
    Patch(facecolor="brown", label="ME")
]

plt.legend(
    handles=legend_elements,
    title="Department"
)


plt.title("Student Network")

plt.show()


print("\nNo. of Students:", g.number_of_nodes())
print("No. of Connections:", g.number_of_edges())
