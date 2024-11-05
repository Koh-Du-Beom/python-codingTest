
T = int(input())

def inner_product(arr1, arr2):
    N = len(arr1)
    result = 0
    for i in range(N):
        result += arr1[i] * arr2[i]
    
    return result

for test in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N > M:
        N, M = M, N
        A, B = B, A
    
    max_val = 0
    
    for i in range(M - N):
        tmp = B[i:i+N]
        res = inner_product(A, tmp)
        if max_val < res:
            max_val = res
     
    print('#{} {}'.format(test, max_val))
        