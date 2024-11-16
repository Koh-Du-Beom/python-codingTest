T = int(input())

def transpose(matrix):
    n = len(matrix)
    transpose = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            transpose[i][j] = matrix[j][i]
    
    return transpose

def cal(matrix, K):
    result = 0 #조건을 만족하는 부분의 개수
    for mat in matrix:
        count = 0 #1의 개수를 세는 변수
        for m in mat:
            if m == 1:
                count +=1
            else:
                count = 0
        
        if count == K:
            result += 1
    
    return result

for test in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    answer = 0
    answer += cal(matrix, K)
    
    transpose_matrix = transpose(matrix)
    answer += cal(transpose_matrix, K)
    
    print('#{} {}'.format(test, answer))
    