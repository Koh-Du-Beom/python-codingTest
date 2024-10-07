def solution(n):
    dp = [0] * (n + 1)  # n+1 크기의 리스트 생성
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] %= 1234567
        
    return dp[n]
