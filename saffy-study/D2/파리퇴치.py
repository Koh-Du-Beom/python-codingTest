T = int(input())

def ret_psum(arr):  # arr에 대한 누적합 배열을 돌려주는 함수
    n = len(arr)
    m = len(arr[0]) if n > 0 else 0
    psum = [[0] * (m+1) for _ in range(n+1)]  # 누적합 배열 선언
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            psum[i][j] = (psum[i-1][j] + psum[i][j-1] - psum[i-1][j-1] 
                           + arr[i-1][j-1])  # 2차원 누적합 계산
    return psum

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    psum = ret_psum(arr)

    max_sum = float('-inf')
    for i in range(N - M + 1):
        for j in range(N - M + 1):
            total = (psum[i+M][j+M] - psum[i+M][j] 
                     - psum[i][j+M] + psum[i][j])
            if total > max_sum:
                max_sum = total

    print('#{} {}'.format(test_case, max_sum))
