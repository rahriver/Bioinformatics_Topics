import matplotlib.pyplot as plt
import networkx as nx

relationships = [
    ("Introduction to Bioinformatics", "Bioinformatics Algorithms", 0.8),
    ("Introduction to Bioinformatics", "Computational Genomics", 0.7),
    ("Introduction to Bioinformatics", "Special Topics in Bioinformatics", 0.5),
    ("Advanced Mathematics and Statistics for Bioinformatics", "Engineering Probability and Statistics", 0.8),
    ("Advanced Topics in Bioinformatics", "Bioinformatics Algorithms", 0.6),
    ("Advanced Topics in Bioinformatics", "Structural Bioinformatics", 0.6),
    ("Algorithmic Game Theory", "Computational Intelligence", 0.7),
    ("Analysis of Biological Networks", "Computational Systems Biology", 0.7),
    ("Bioinformatics Database Systems", "Massive Biological Data Analysis", 0.6),
    ("Bioinformatics Database Systems", "Structural Bioinformatics", 0.6),
    ("Cellular and Molecular Biology", "Cellular and Molecular Biology Laboratory", 0.8),
    ("Chemistry for Life Science", "Computational Drug Design", 0.7),
    ("Computational Evolutionary Biology", "Genetic and Evolution", 0.8),
    ("Computational Systems Biology", "Multi-scale Modeling of Biological Systems", 0.7),
    ("Convex Optimization", "Probabilistic Graphical Models", 0.6),
    ("Deep Learning", "Bioinformatics Algorithms", 0.7),
    ("Deep Learning", "Computational Intelligence", 0.8),
    ("Bioinformatics Algorithms", "Computational Genomics", 0.7),
    ("Medical Informatics", "Bioinformatics Database Systems", 0.6),
    ("Medical Informatics", "Structural Bioinformatics", 0.5),
    ("Parallel Processing", "Bioinformatics Database Systems", 0.6),
    ("Parallel Processing", "Massive Biological Data Analysis", 0.7),
    ("Probabilistic Graphical Models", "Stochastic Processes In Bioinformatics", 0.6),
    ("Stochastic Processes In Bioinformatics", "Analysis of Biological Networks", 0.5),
    ("Structural Bioinformatics", "Computational Drug Design", 0.6)
]

G = nx.DiGraph()

for relationship in relationships:
    topic1, topic2, score = relationship
    G.add_edge(topic1, topic2, weight=score)

sizes = nx.degree_centrality(G)
sizes = [v * 10000 + 500 for v in sizes.values()]

pos = nx.spring_layout(G, k=1.5, iterations=120)
nx.draw_networkx_nodes(G, pos, node_size=sizes, node_color="#ff7c7c", alpha=0.8)
nx.draw_networkx_edges(G, pos, width=1, alpha=0.5)
nx.draw_networkx_labels(G, pos, font_size=9, font_family="Roboto")

plt.title("Bioinformatics Chart | Relationships")
plt.axis("off")
plt.tight_layout()
plt.savefig("bio.png")
plt.show()
