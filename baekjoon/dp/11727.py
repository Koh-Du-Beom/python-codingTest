N = int(input())
dp = [0] * (N + 2)  # N이 0일 때를 대비해 크기를 N+2로 설정
dp[0] = 1
dp[1] = 1

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + dp[i - 2] * 2

print(dp[N])