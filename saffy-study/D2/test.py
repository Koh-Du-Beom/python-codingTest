
T = int(input())    

def ret_psum(arr): #arr에 대한 누적합배열을 돌려주는 함수
    n = len(arr)
    psum = [[0 for _ in range(n+1)] for _ in range(n+1)] #누적합 배열 선언
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            psum[i][j] = psum[i-1][j-1] + arr[i][j] - (psum[i-1][j] + psum[i][j-1]) #2차원 배열로 누적합 배열 만들기
    return sum
		         

for i in range(1, T+1):
    N, M = map(int, input().split())
    arr = [map(int, input().split()) for _ in range(N)]
    psum = ret_psum(arr)
    
    max = 0
    for i in range(M):
        for j in range(M):
            if max < psum[i][j] + psum[i+3][j+3] - (psum[i+3][j] + psum[i][j+3]):
                max = psum[i][j] + psum[i+3][j+3] - (psum[i+3][j] + psum[i][j+3])
    
    print('#{} {}'.format(i, max))