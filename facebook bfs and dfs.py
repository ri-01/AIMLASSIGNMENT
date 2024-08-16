import networkx as nx  #https://www.geeksforgeeks.org/networkx-python-software-package-study-complex-networks/
import matplotlib.pyplot as plt

# Load the dataset
# Assuming the dataset is in a file called 'facebook_combined.txt'
# The file contains edges in the format: node1 node2

G = nx.read_edgelist('facebook_combined.txt')

# Basic info about the graph
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")
print(f"Is the graph directed: {G.is_directed()}")
print(f"Graph density: {nx.density(G)}")

# Define start and goal nodes
start_node = '0'  # Example start node
goal_node = '100'  # Example goal node

# Ensure start_node and goal_node are in the graph
if start_node not in G or goal_node not in G:
    raise ValueError("Start or goal node not in graph")
from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])  # Queue of tuples (node, path)

    while queue:
        current_node, path = queue.popleft()
        if current_node == goal:
            return path
        if current_node not in visited:
            visited.add(current_node)
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.append((neighbor, new_path))
    return None

path= bfs(G,'12','1000')
print("Path :", path)
def dfs(graph, start):
    stack = [(start, [start])]  
    visited = set()
    all_paths = []

    while stack:
        current_node, path = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            all_paths.append(path)  
            for neighbor in graph.neighbors(current_node):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    stack.append((neighbor, new_path))
    return all_paths
path= dfs(G,'12')
p=set()
for i in path:
    p.update(i)
print("Number of nodes Reachable from 12: ", len(p))
def visualize_bfs(G, bfs_path):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

    if bfs_path:
        path_edges = list(zip(bfs_path, bfs_path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=bfs_path, node_color='orange')
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='orange', width=2)

    plt.show()
bfs_path = bfs(G, start_node, goal_node)
visualize_bfs(G, bfs_path)
def visualize_dfs(G, dfs_visited):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold')

    if dfs_visited:
        nx.draw_networkx_nodes(G, pos, nodelist=dfs_visited, node_color='green')
        nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black')

    plt.show()
dfs_visited = dfs(G, start_node)
visualize_dfs(G, dfs_visited)