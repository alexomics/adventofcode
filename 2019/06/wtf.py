import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
[G.add_edge(*l.strip().split(")")) for l in open("input.txt")]
print(f"Part 1: {nx.transitive_closure(G).size()}\nPart 2: {nx.shortest_path_length(G.to_undirected(), 'YOU', 'SAN')-2}")

pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=50)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, arrows=True)
plt.show()
