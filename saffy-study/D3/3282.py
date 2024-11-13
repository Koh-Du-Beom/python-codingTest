T = int(input())

def DFS(v, volume, cost):
  global knapsack, max_value, visited, N, K
  
  if K < volume:
    return
  
  max_value = max(max_value, cost)
  for i in range(v + 1, len(knapsack)):
    visited[i] = True
    DFS(i + 1, volume + knapsack[i][0], cost + knapsack[i][1])
    visited[i] = False

for test in range(1, T + 1):
  N, K = map(int, input().split())

  knapsack = []
  for _ in range(N):
    V, C = map(int, input().split())
    knapsack.append((V, C))
  
  max_value = 0
  visited = [False] * N
  for i in range(N):
    visited[i] = True
    DFS(i, knapsack[i][0], knapsack[i][1])
    visited[i] = False

  print('#{} {}'.format(test, max_value))