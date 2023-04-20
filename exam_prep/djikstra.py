graph = {
    'a':{'b':3,'c':2,'d':4},
    'b':{'c':2,'d':4},
    'c':{'d':4,'e':6},
    'd':{'e':4},
    'e':{'e':3}
}

def djikstra(graph,start,goal):
    shortest_distance={}
    track_predecessor={}
    unseenNodes = graph
    infinity = 99999
    track_path = []

    for node in unseenNodes:
        shortest_distance[node]=infinity
    shortest_distance[start]=0

    while unseenNodes:
        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node,weight in path_options:
            if weight+shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight+shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node
        
        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]
        except KeyError:
            print('Not reachable')
            break

    track_path.insert(0, start)

    print("shortest distance is: " + str(shortest_distance[goal]))
    print("optimal path is: " + str(track_path))

djikstra(graph,'a','e')