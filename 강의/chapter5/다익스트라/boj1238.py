import sys
from queue import PriorityQueue
input = sys.stdin.readline

INF = int(1e12)

def dijkstra(start_node):
  global N, adj_list
  
  dist = [INF] * (N + 1)
  pq = PriorityQueue()
  dist[start_node] = 0
  pq.put([0, start_node])
  
  while not pq.empty():
    cur_dist, cur_node = pq.get()
    for adj_node, adj_dist in adj_list[cur_node]:
      temp_dist = adj_dist + cur_dist
      if temp_dist < dist[adj_node]:
        dist[adj_node] = temp_dist
        pq.put([temp_dist, adj_node])
  return dist

N, M, X = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for _ in range(M):
  s, e, t = map(int, input().split())
  adj_list[s].append([e, t])
  
dist = [INF] * (N + 1)
for i in range(1, N + 1):
  dist[i] = dijkstra(i)
  
ans = -1
for i in range(1, N + 1):
  ans = max(ans, dist[i][X] + dist[X][i])  #왕복
  
print(ans)