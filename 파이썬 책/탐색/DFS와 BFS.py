from collections import deque
N, M, START = map(int, input().split())
A = [[] for _ in range(N + 1)]

for _ in range(N):
  start, end = map(int, input().split())
  A[start].append(end); A[end].append(start)

for i in range(N+1):
  A[i].sort()
  
def DFS(v):
  print(v, end="")
  visited[v] = True
  for i in A[v]:
    if not visited[i]:
      DFS(i)

visited = [False]
 

visited = [False] * (N+1)
DFS(START)

def BFS(v):
  my_deque = deque()
  my_deque.append(v)
  visited[v] = True
  while my_deque:
    now_node = my_deque.popleft()
    print(now_node, end=' ')
    for i in A[now_node]:
      if not visited[i]:
        visited[i] = True
        my_deque.append(i)

print()
visited = [False]*(N+1)
BFS(START)
  