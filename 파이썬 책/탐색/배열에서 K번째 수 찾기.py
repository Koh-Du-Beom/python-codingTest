import sys
input = sys.stdin.readline

N = int(input())
k = int(input())

A = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        A[i][j] = (i+1) * (j+1)

print(A)