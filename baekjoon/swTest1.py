from collections import deque

def BFS(N, M):
  queue = deque()
  queue.append((0, 0))
  
  visited = set()
  while queue:
    position, moves = queue.popleft()
    
    if position == M:
      return moves
    
    nexts = [position + 1, position + 6, position * 2]
    for next in nexts:
      if 0 <= next <= N and next not in visited:
        visited.add(position)
        queue.append((next, moves + 1))
  
  return -1


	
N, M = map(int, input().split())
print(BFS(N, M))



