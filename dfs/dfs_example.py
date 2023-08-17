#!/usr/bin/env python
from dfs import DepthFirstSearch

dfs = DepthFirstSearch()

# Example graph (same as above) as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
print('DFS working ===============')
dfs.dfs(graph, 'A')
print('')

print('DFS max depth search')
max_depth = dfs.tree_max_depth(graph, 'A')
print('Max depth: ' + str(max_depth))
print('')

graph_2 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': ['G'],
    'G': ['H'],
    'H': []
}
print('DFS working ===============')
dfs.dfs(graph_2, 'A')
print('')

print('DFS max depth search')
max_depth_2 = dfs.tree_max_depth(graph_2, 'A')
print('Max depth for graph_2: ' + str(max_depth_2))
print('')

# Example graph (same as above) as an adjacency list
graph = {
    5: [4, 6],
    4: [3, 8],
    3: [],
    8: [],
    6: []
}

visible_nodes_list = dfs.visible_nodes(graph, 5)
print("Visible Nodes:", str(visible_nodes_list))
