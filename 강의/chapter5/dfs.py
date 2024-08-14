
def DFS(v):
    global adj_list, visited
    
    if visited[v]:
        return

    visited[v] = True
    print(v, end=' ')
    
    for adj_node in adj_list[v]:
        DFS(adj_node)

adj_list = [[] for _ in range(5)]
visited = [False] * 5

adj_list[0].append(1); adj_list[0].append(2)
adj_list[1].append(4); adj_list[1].append(3)
adj_list[2].append(3)
adj_list[3].append(0)

DFS(0)