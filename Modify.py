import networkx as nx
import matplotlib.pyplot as plt

import pandas as pd
import string

# Read data from file
user = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\Revised_Tags.csv')

# Create dictionary of mentions for each user
final = {}
for i in range(0, 542):
    dic = {}
    for j in range(len(user['Tags'][i])):
        mention = user['Tags'][i][j][0]
        count = user['Tags'][i][j][1]
        mention = mention.lower().translate(str.maketrans('', '', string.punctuation.replace('@', '')))
        mention = mention.replace('_', '')
        if mention.startswith('@'):
            # Check if mention is soniagandhfc
            if mention == '@soniagandhifc':
                continue
            dic[mention] = count
    username = user['Username'][i].lower().replace('_', '')
    # Check if username is soniagandhfc
    if username == '@soniagandhifc':
        continue
    final[username] = dic

# Create graph from dictionary of mentions
G = nx.Graph()
for person, mentions in final.items():
    for mention in mentions:
        G.add_edge(person, mention)

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Print centrality measures for the top 10 nodes for each centrality measure
print("Degree centrality:")
degree_top_10 = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
print(degree_top_10)
print("Betweenness centrality:")
betweenness_top_10 = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
print(betweenness_top_10)
print("Eigenvector centrality:")
eigenvector_top_10 = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:10]
print(eigenvector_top_10)

# Create separate lists for different centrality values
degree_list = [tup[1] for tup in degree_top_10]
degree_persons = [tup[0] for tup in degree_top_10]

betweenness_list = [tup[1] for tup in betweenness_top_10]
betweenness_persons = [tup[0] for tup in betweenness_top_10]

eigenvector_list = [tup[1] for tup in eigenvector_top_10]
eigenvector_persons = [tup[0] for tup in eigenvector_top_10]

# Identify communities
communities = nx.algorithms.community.greedy_modularity_communities(G)
print("Communities:")
print(communities)

# Visualize the graph
pos = nx.spring_layout(G)
node_color = [color for node, color in degree_centrality.items() if degree_centrality[node] >= 0.07]
nx.draw_networkx_nodes(G, pos, node_size=5, cmap=plt.cm.RdYlBu, node_color=node_color)
nx.draw_networkx_edges(G, pos, edge_color='lightblue')
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')
plt.axis('off')
plt.show()
