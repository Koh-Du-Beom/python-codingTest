def DFS(v, depth):
    global adj_list, visited, max_length
    visited[v] = True
    max_length = max(max_length, depth)

    for adj_node in adj_list[v]:
        if not visited[adj_node]:
            DFS(adj_node, depth + 1)

    visited[v] = False  # 백트래킹을 위해 방문 표시를 해제

T = int(input())
for test in range(1, T + 1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]

    for i in range(M):
        start, end = map(int, input().split())
        adj_list[start].append(end)
        adj_list[end].append(start)

    max_length = 1
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        DFS(i, 1)

    print('#{} {}'.format(test, max_length))
