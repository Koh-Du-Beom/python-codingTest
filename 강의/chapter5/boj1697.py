import sys
from collections import deque
input = sys.stdin.readline

def BFS():
  global N, K, visited, MAX
  queue = deque()
  
  queue.append((0, N))
  visited[N] = True
  while queue:
    time, pos = queue.popleft()
    
    if pos == K:
      print(time)
      return
    
    for next_pos in [pos - 1, pos + 1, pos * 2]:
      if (0 <= next_pos <= MAX) and (not visited[next_pos]):
        queue.append((time + 1, next_pos))
        visited[next_pos] = True

MAX = int(1e5)
N, K = map(int, input().split())
visited = [False] * (MAX + 1)

BFS()
