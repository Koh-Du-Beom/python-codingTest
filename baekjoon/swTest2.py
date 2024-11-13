
N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]

for digit in range(10):
  dp[1][digit] = 1

for length in range(2, N + 1):
  for digit in range(10):
    dp[length][digit] = sum(dp[length-1][digit:])

print(sum(dp[N]))