import sys
input = sys.stdin.readline

def factorial(n):
  dp = [1] *(n + 1)
  for i in range(2, n + 1):
    dp[i] = i * dp[i - 1]
  
  return dp[n]

N, K = map(int, input().split())

print((factorial(N) // (factorial(N - K) * factorial(K))) % 10007)

