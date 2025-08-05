import networkx as nx

def graph_connections(connections):
    graph = nx.Graph()
    for connection in connections:
        graph.add_edge(connection[0], connection[1])
    return graph

if __name__ == '__main__':
    with open('input', 'r') as file:
        lines = file.readlines()
        connections = [tuple(line.strip().split('-')) for line in lines]

    connection_graph = graph_connections(connections)

    lans = list(nx.find_cliques(connection_graph)) #The entire problem completed in one line

    largest_lan = max(lans, key=len)

    largest_lan = sorted(largest_lan)

    answer = ','.join(largest_lan)

    print(answer)