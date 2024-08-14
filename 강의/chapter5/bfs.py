from collections import deque

def BFS(v):
    global adj_list, visited, my_deque
    my_deque.append(v)
    visited[v] = True
    while my_deque:
        now_node = my_deque.popleft()
        print(now_node, end=' ')
        for adj_node in adj_list[now_node]:
            if not visited[adj_node]:
                visited[adj_node] = True
                my_deque.append(adj_node)


N = 5
adj_list = [[] for _ in range(N)]
visited = [False] * N
my_deque = deque()

adj_list[0].append(1); adj_list[0].append(2)
adj_list[1].append(4); adj_list[1].append(3)
adj_list[2].append(3)
adj_list[3].append(0)

BFS(0)