import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# 입력 받기
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# 스택을 사용한 DFS 함수 정의
def DFS(v):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            for neighbor in A[node]:
                if not visited[neighbor]:
                    stack.append(neighbor)

# 간선 정보 입력 받기
for _ in range(m):
    start, end = map(int, input().split())
    A[start].append(end)
    A[end].append(start)

count = 0

# 모든 정점에 대해 방문 여부 체크
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

# 결과 출력
print(count)
