
T = int(input())

def DFS(v, total_point, total_cal):
    global food_infos, max_point, visited, L

    if total_cal > L:
        return

    max_point = max(max_point, total_point)
    for i in range(v + 1, len(food_infos)):
        if not visited[i]:
            visited[i] = True
            DFS(i, total_point + food_infos[i][0], total_cal + food_infos[i][1])
            visited[i] = False  # 백트래킹

for test in range(1, T + 1):
    N, L = map(int, input().split())

    food_infos = []
    for _ in range(N):
        point, cal = map(int, input().split())
        food_infos.append((point, cal))

    max_point = 0
    visited = [False] * N
    for i in range(N):
        visited[i] = True
        DFS(i, food_infos[i][0], food_infos[i][1])
        visited[i] = False

    print('{} {}'.format(test, max_point))

