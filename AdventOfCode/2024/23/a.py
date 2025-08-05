import networkx as nx

def graph_connections(connections):
    graph = nx.Graph()
    for connection in connections:
        graph.add_edge(connection[0], connection[1])
    return graph    

def find_triangles_directed(graph: nx.Graph):
    triangles = set()
    for u in graph.nodes:
        for v in graph.neighbors(u):
            for w in graph.neighbors(v):
                if w != u and graph.has_edge(w, u):
                    triangle = tuple(sorted([u, v, w]))
                    triangles.add(triangle)
    return list(triangles)

if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        connections = [tuple(line.strip().split('-')) for line in lines]

    connection_graph = graph_connections(connections)

    cycles = find_triangles_directed(connection_graph)

    count = 0
    for cycle in cycles:
        if any(node.startswith('t') for node in cycle):
            count += 1 
    
    print(count)