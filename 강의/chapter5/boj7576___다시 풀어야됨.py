import sys
from collections import deque
input = sys.stdin.readline

INF = int(1e12)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
time = [[INF] * M for _ in range(N)]
queue = deque()

for y in range(N):
  for x in range(M):
    if matrix[y][x] == 1:
      queue.append((y, x))
      time[y][x] = 0

while queue:
  y, x = queue.popleft()
  
  nxts = [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]
  for ny, nx in nxts:
    if not (0 <= ny < N and 0 <= nx < M):
      continue
    if time[ny][nx] <= time[y][x] + 1:
      continue
    if matrix[ny][nx] == -1:
      continue
    queue.append((ny, nx))
    time[ny][nx] = time[y][x] + 1

ans = -1
for y in range(N):
  for x in range(M):
    if matrix[y][x] != -1:
      ans = max(ans, time[y][x])

print(ans if ans != INF else -1)