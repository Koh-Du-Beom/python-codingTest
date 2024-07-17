from collections import deque

dx = [0, 1, 0, -1]
dy = [0, 1, 0, -1]
N, M = map(int, input().split())
A = [[0] * M for _ in range(M)]
visited = [[False] * M for _ in range(M)]

for i in range(N):
  numbers = list(input())
  for j in range(M):
    A[i][j] = int(numbers[j])
    
def BFS(i, j):
  my_deque = deque()
  my_deque.append((i, j))
  visited[i][j] = True
  while(my_deque):
    now_node = my_deque.popleft()
    for k in range(4):
      x = now_node[0] + dx[k]
      y = now_node[0] + dy[k]
      if x>=0 and y >=0 and x<N and y<M:
        if A[x][y] != 0 and not visited[x][y]:
          visited[x][y] = True
          A[x][y] = A[now_node[0]][now_node[1]] + 1
          my_deque.append((x, y))

BFS(0 ,0)
print(A[N-1][M-1])