def dijkstra_algorithm(graph, start_node):
    shortest_path = {}
    previous_nodes = {}
    unvisited_nodes = list(graph.vertices)
    for node in graph.vertices:
        shortest_path[node] = float('inf')
    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        for neighbor in current_min_node.edges:
            tentative_value = shortest[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)
    return previous_nodes, shortest_path
