T = int(input())

def factorial(n):
    dp = [1] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = i * dp[i-1]
    
    return dp[n]

def combination_cnt(N, R):
    return factorial(N) // (factorial(N-R) * factorial(R))

print(factorial(5))

for test in range(1, T + 1):
    N, R = map(int, input().split())
    print('#{} {}'.format(test, combination_cnt(N, R)))
