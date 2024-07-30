import sys
input = sys.stdin.readline

def get_max(y, x):
    global N, matrix
    best = 0
    
    #column
    bef = '-'
    value = 0
    for j in range(N):
        if bef == matrix[y][j]:
            value += 1
        else:
            value = 1
        bef = matrix[y][j]
        best = max(best, value)
        
    #row
    bef = '-'
    value = 0
    for i in range(N):
        if bef == matrix[i][x]:
            value += 1
        else:
            value = 1
        bef = matrix[i][x]
        best = max(best, value)

    return best       
        
    
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
matrix = [list(input()) for _ in range(N)]
ans = 0

for y in range(N):
    for x in range(N):
        if y == x :
            ans = max(ans, get_max(y, x))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
               if matrix[y][x] != matrix[ny][nx]:
                   matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x] #바꾸고
                   ans = max(ans, get_max(y, x)) #검사하고
                   matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x] #원상태 복구

print(ans)