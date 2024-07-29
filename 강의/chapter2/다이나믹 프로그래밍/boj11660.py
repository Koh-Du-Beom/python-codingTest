import sys
input = sys.stdin.readline

def get_sum(sy, sx, ey, ex):
    global psum
    return psum[ey][ex] - (psum[ey][sx - 1] + psum[sy - 1][ex] - psum[sy - 1][sx - 1])

N, M = map(int, input().split())

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    arr[i][1:] = list(map(int, input().split()))
    #arr배열 받기
  
psum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        psum[i][j] = (psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1]) + arr[i][j]
        #누적합 배열 만들기

result_arr = []
for j in range(M):
    sy, sx, ey, ex = map(int, input().split())
    result = get_sum(sy,sx, ey, ex)
    result_arr.append(result)

for result in result_arr:
    print(result)

