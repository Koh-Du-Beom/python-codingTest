import sys
from collections import deque

def BFS():
  queue = deque()
  global visited, matrix, dy, dx
  
  queue.append((1,1,1))
  visited[1][1] = True
  
  while queue:
    dist, y, x = queue.popleft()
    
    if y == N and x == M:
      print(dist)
      return

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (1 <= ny <= N and 1 <= nx <= M) and (not visited[ny][nx]) and (matrix[ny][nx] == '1'):
        queue.append((dist + 1, ny, nx))
        visited[ny][nx] = True

  print(-1)
  
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
matrix = matrix = ['0' * (M + 1)] + ['0' + input() for _ in range(N)]
visited = [[False] * (M + 1) for _ in range(N + 1)]

BFS()