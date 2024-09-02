import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
  queue = deque()
  global visited, adj_list, count

  queue.append(v)
  visited[v] = True
  
  while queue:
    node = queue.popleft()
    count += 1
    
    for adj_node in adj_list[node]:
      if visited[adj_node]:
        continue
      queue.append(adj_node)
      visited[adj_node] = True
  
def DFS(v):
  global visited, adj_list, count
  
  visited[v] = True
    
  
N = int(input())
M = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for i in range(M):
  start, end = map(int, input().split())
  adj_list[start].append(end)
  adj_list[end].append(start)

BFS(1)

print(count - 1)
  