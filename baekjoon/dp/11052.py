import sys
input = sys.stdin.readline

N = int(input())  # 카드의 개수
P = [0] + list(map(int, input().split()))  # 카드팩 가격 (1-based index)

# DP 배열 초기화
dp = [0] * (N + 1)

for i in range(1, N + 1):
  for k in range(1, i + 1):
    dp[i] = max(dp[i], dp[i-k] + P[k])

print(dp[N])