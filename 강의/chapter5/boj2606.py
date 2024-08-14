import sys
input = sys.stdin.readline

def DFS(node):
    global adj_list, visited, count
    
    if visited[node]:
        return
    
    visited[node] = True
    count += 1
    
    for adj_node in adj_list[node]:
        DFS(adj_node)
    

N = int(input())
M = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

DFS(1)
print(count - 1)