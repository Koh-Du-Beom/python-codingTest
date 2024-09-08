from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(maps, y, x, n, m, visited):
    visited[y][x] = True
    queue = deque()
    queue.append([y, x])
    days = int(maps[y][x])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and maps[ny][nx] != 'X':
                visited[ny][nx] = True
                queue.append([ny, nx])
                days += int(maps[ny][nx])
    
    return days

def solution(maps):
    answer = []
    n, m = len(maps), len(maps[0]) 
    visited = [[False] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(maps, i, j, n, m, visited))
    
    if answer:
        return sorted(answer)
    else:
        return [-1]
  
