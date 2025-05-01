from collections import defaultdict

# Read the file and put keylogs into adjacency list {dictionary}, using a set also reduces duplicates
# Reason behind adjacency list, it helps me with direction and the constraints for the graph to be one directional

def create_graph(file):

    with open(file,"r") as file:
        keylogs = [line.strip() for line in file if line.strip()]
        
    graph = defaultdict(set)
    nodes = set()
    
    for line in keylogs:
        a, b, c = line
        graph[a].add(b)
        graph[b].add(c)
        nodes.update([a,b,c])
        
    # If the node have no children, then have it set to default "set()"    
    for node in nodes:
        graph.setdefault(node, set())        
        
    return graph

# Do DFS and Topological Sort on said list and get answer

def dfs(node, graph, visited, order):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited, order)
    order.append(node)
    
def topological_sort(graph):
    visited = set()
    order = []
    
    for node in graph:
        if node not in visited:
            dfs(node, graph, visited, order)
            
    order.reverse()
    return ''.join(order)

if __name__ == "__main__":
    graphTest = create_graph("10_test.txt")
    print("Test case: " + topological_sort(graphTest))
    
    graph = create_graph("10.txt")
    print("Answer: " + topological_sort(graph))