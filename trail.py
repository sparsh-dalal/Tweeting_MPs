import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import string

# Define the list of MPs you want to focus on
mp_list = ['@supriya_sule', '@narendramodi', '@ombirlakota']

# Load the data
user = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\Revised_Tags.csv')

# Filter the data to only include MPs in mp_list
user = user[user['Username'].isin(mp_list)]

# Create a dictionary to store the mentions for each MP in mp_list
final = {}
for i in range(len(user)):
    dic = {}
    for j in range(len(user['Tags'].iloc[i])):
        mention = user['Tags'].iloc[i][j][0]
        count = user['Tags'].iloc[i][j][1]
        mention = mention.lower().translate(str.maketrans('', '', string.punctuation.replace('@', '')))
        if mention.startswith('@') and mention in mp_list:
            dic[mention] = count
    final[user['Username'].iloc[i].lower()] = dic

# Create a new graph
G = nx.Graph()

# Add edges for the mentions between MPs in mp_list
for person, mentions in final.items():
    for mention in mentions:
        G.add_edge(person, mention)

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)

# Print centrality measures for the top 10 nodes
print("Top 10 nodes by degree centrality:")
print(sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:10])
print("Top 10 nodes by betweenness centrality:")
print(sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:10])
print("Top 10 nodes by eigenvector centrality:")
print(sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:10])

# Identify communities
communities = nx.algorithms.community.greedy_modularity_communities(G)
print("Communities:")
print(communities)

# Visualize the graph
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=100, cmap=plt.cm.RdYlBu, node_color=list(degree_centrality.values()))
nx.draw_networkx_edges(G, pos, edge_color='lightblue')
nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')
plt.axis('off')
plt.show()