import sys
from collections import deque
input = sys.stdin.readline

def BFS(sy, sx, h):
  global dy, dx, N, matrix, visited
  queue = deque()
  
  queue.append((sy, sx))
  visited[sy][sx] = True
  
  while queue:
    y, x = queue.popleft()
    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]
      if (0 <= ny < N and 0 <= nx < N) and (not visited[ny][ny]) and (matrix[ny][nx] > h):
        queue.append((ny, nx))
        visited[ny][nx] = True

def get_num(height):
  global dy, dx, N, matrix, visited
  
  visited = [[False] * N for _ in range(N)]
  
  num = 0
  for sy in range(N):
    for sx in range(N):
      if not visited[sy][sx] and matrix[sy][sx] > height:
        BFS(sy, sx, height)
        num += 1

  return num

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for height in range(101):
  ans = max(ans, get_num(height))

print(ans)