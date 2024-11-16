N = int(input())

adj_list = [[] for _ in range(N + 1)]

for _ in range(N):
  start, end = map(int, input().split())
  adj_list[start].append(end)

print(adj_list)