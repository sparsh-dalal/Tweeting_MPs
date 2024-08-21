import networkx as nx
import matplotlib.pyplot as plt

import pandas as pd
import string
G = nx.Graph()

user = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\Revised_Tags.csv')
df = pd.read_csv(r'C:\Users\dalal\PycharmProjects\Tweepy\MP_list(No of tweets).csv')
b = df['Username']



df2 = pd.read_pickle(r'C:\Users\dalal\PycharmProjects\Tweepy\Runining_Files\oui.csv')
f = list(df2['oui'])

print(f)



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
            if mention in f or mention == '' or mention == '@kavitasinghmp':
                print(mention)
                continue

            dic[mention] = count
    username = user['Username'][i].lower().replace('_', '')
    # Check if username is soniagandhfc
    if username in f or username == '@soniagandhfc':
        continue
    final[username] = dic






G = nx.Graph()


for person, mentions in final.items():
    for mention in mentions:
        G.add_edge(person, mention)

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
eigenvector_centrality = nx.eigenvector_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

print("Degree centrality:")
print(sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:15])
degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:15]
print("Betweenness centrality:")
print(sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:15])
between = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)[:15]
print("Eigenvector centrality:")
print(sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:15])
eigen = sorted(eigenvector_centrality.items(), key=lambda x: x[1], reverse=True)[:15]
closeness = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)[:15]
print("Closeness centrality:")
print(closeness)

xyz = {}
for a in range(len(degree)):
    xyz[degree[a][0]] = []
    xyz[degree[a][0]].append(degree[a][1])

for a in range(len(between)):
    if between[a][0] in xyz.keys():
        xyz[between[a][0]].append(between[a][1])
    else:
        xyz[between[a][0]] = [-1, between[a][1]]


for a in range(len(closeness)):
    if closeness[a][0] in xyz.keys():
        xyz[closeness[a][0]].append(closeness[a][1])
    else:
        xyz[closeness[a][0]] = [-1, -1, closeness[a][1]]

for a in range(len(eigen)):
    if eigen[a][0] in xyz.keys():
        xyz[eigen[a][0]].append(eigen[a][1])
    else:
        xyz[eigen[a][0]] = [-1, -1, -1, eigen[a][1]]

print(xyz.keys())



# x = [item[0] for item in degree]
# y = [item[1] for item in degree]
# fig = plt.figure(facecolor='black')
# ax = fig.add_subplot(111, facecolor='black')
#
# ax.bar(x, y)
# ax.set_ylim(0, 1)
#
# ax.set_xlabel('MPs', color='white',fontsize=25)
# ax.set_ylabel('Degree Centrality', color='white', fontsize=25)
# ax.xaxis.label.set_color('white')
# ax.yaxis.label.set_color('white')
#
# ax.tick_params(axis='y', colors='white')
#
# ax.set_title('')
#
# for i in range(len(x)):
#     ax.text(i, 0.0, x[i], rotation=90, ha='center', va='bottom', fontsize=25, color='white')
#
# ax.set_xticks([])
#
# plt.show()
#
#
#
#
# plt.xticks([])  # removes x-axis labels
# plt.show()
#
#
# x = [item[0] for item in between]
# y = [item[1] for item in between]
#
# plt.bar(x, y)
# plt.ylim(0,0.3)
#
#
# plt.xlabel('MPs')
# plt.ylabel('Betweenness Centrality')
# plt.title('')
#
# for i in range(len(x)):
#     plt.text(i, y[i], x[i], rotation=90, ha='center', va='bottom', fontsize=12)
#
# plt.xticks([])  # removes x-axis labels
# plt.show()
#
# x = [item[0] for item in eigen]
# y = [item[1] for item in eigen]
#
# plt.bar(x, y)
# plt.ylim(0,0.2)
#
#
# plt.xlabel('MPs')
# plt.ylabel('Eigenvector Centrality')
# plt.title('')
#
# for i in range(len(x)):
#     plt.text(i, y[i], x[i], rotation=90, ha='center', va='bottom', fontsize=12)
#
# plt.xticks([])  # removes x-axis labels
# plt.show()
#
# x = [item[0] for item in closeness]
# y = [item[1] for item in closeness]
#
# plt.bar(x, y)
# plt.ylim(0,1)
#
#
# plt.xlabel('MPs')
# plt.ylabel('Closeness Centrality')
# plt.title('')
#
# for i in range(len(x)):
#     plt.text(i, y[i], x[i], rotation=90, ha='center', va='bottom', fontsize=12)
#
# plt.xticks([])  # removes x-axis labels
# plt.show()
# degree = []
# for i in range(0,542):
#     count = 0
#     for j in range(len(degree_centrality.keys())):
#         l= list(degree_centrality.keys())
#
#         table = str.maketrans('', '', string.punctuation.replace('#', '').replace('@', ''))
#         # Remove all punctuation except for # and @ symbols and convert to lowercase
#         za = b[i].translate(table).lower()
#         if za == l[j]:
#             w = list(degree_centrality.values())
#             degree.append(w[j])
#             count = count + 1
#     if count ==0:
#         degree.append('0')
#
#
# print(betweenness_centrality.items())
# between = []
# for i in range(0, 542):
#     count = 0
#     for j in range(len(betweenness_centrality.keys())):
#         l = list(betweenness_centrality.keys())
#         table = str.maketrans('', '', string.punctuation.replace('#', '').replace('@', ''))
#         # Remove all punctuation except for # and @ symbols and convert to lowercase
#         za = b[i].translate(table).lower()
#         if za == l[j]:
#             w = list(betweenness_centrality.values())
#             between.append(w[j])
#             count = count + 1
#     if count == 0:
#         between.append('0')
# print(between)
# eigen = []
# for i in range(0, 542):
#     count = 0
#     for j in range(len(eigenvector_centrality.keys())):
#         l = list(eigenvector_centrality.keys())
#
#         table = str.maketrans('', '', string.punctuation.replace('#', '').replace('@', ''))
#         # Remove all punctuation except for # and @ symbols and convert to lowercase
#         za = b[i].translate(table).lower()
#         if za == l[j]:
#             w = list(eigenvector_centrality.values())
#             eigen.append(w[j])
#             count = count + 1
#     if count == 0:
#         eigen.append('0')
#
# print(eigen)
#
# closeness = []
# for i in range(0,542):
#     count = 0
#     for j in range(len(closeness_centrality.keys())):
#         l= list(closeness_centrality.keys())
#
#         table = str.maketrans('', '', string.punctuation.replace('#', '').replace('@', ''))
#         # Remove all punctuation except for # and @ symbols and convert to lowercase
#         za = b[i].translate(table).lower()
#         if za == l[j]:
#             w = list(closeness_centrality.values())
#             closeness.append(w[j])
#             count = count + 1
#     if count ==0:
#         closeness.append('0')
#
# print(closeness)
#
# # Identify communities
#
# df['Degree'] = degree
# df['Between'] = between
# df['Closeness'] = closeness
# df['Eigen'] = eigen
#
# df.to_csv('Statistics.csv')





# subgraphs = []
# for community in communities:
#     subgraph = G.subgraph(community)
#     subgraphs.append(subgraph)
#
# # Visualize each subgraph separately
# pos = nx.spring_layout(G)
# for i, subgraph in enumerate(subgraphs):
#     plt.figure(i+1)
#     plt.title(f"Community {i+1}")
#     nx.draw_networkx(subgraph, pos=pos, node_size=100, cmap=plt.cm.RdYlBu, with_labels=True)
#     plt.axis('off')
#
# # Show all subgraphs
# plt.show()



# Visualize the graph


# pos = nx.spring_layout(G)
# node_color = [color for node, color in degree_centrality.items() if degree_centrality[node] >= 0.07]
# #node_size = [size for node, size in node_sizes.items() if degree_centrality[node] >= 0.07]
# nx.draw_networkx_nodes(G, pos, node_size=5, cmap=plt.cm.RdYlBu, node_color=node_color)
# nx.draw_networkx_edges(G, pos, edge_color='lightblue')
# nx.draw_networkx_labels(G, pos, font_size=8, font_family='sans-serif')
# plt.axis('off')
# plt.show()

