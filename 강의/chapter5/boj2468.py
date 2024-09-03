from collections import deque


def bfs(sy, sx, h):
	global dy, dx, N, matrix, visited

	q = deque()
	q.append((sy, sx))
	visited[sy][sx] = True

	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = y + dy[i]
			nx = x + dx[i]
			if (0 <= ny < N and 0 <= nx < N) and (not visited[ny][nx]) and(matrix[ny][nx] > h):
				q.append((ny, nx))
				visited[ny][nx] = True


def get_num(height): # 높이가 height일 때, 안전 영역의 개수를 반환
	global dy, dx, N, matrix, visited

	visited = [[False] * N for _ in range(N)]

	num = 0
	for sy in range(N):
		for sx in range(N):
			if (not visited[sy][sx]) and (matrix[sy][sx] > height):
				bfs(sy, sx, height)
				num += 1

	return num


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

# input
N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
ans = 0
for height in range(101):
	ans = max(ans, get_num(height))

print(ans)
