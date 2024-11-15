import sys
input = sys.stdin.readline

N, K = map(int, input().split()) #N은 가방 수, K는 견디는 최대무게

dp = [0] * (K + 1)

for _ in range(N): #무게와 가치 입력받기 
  W, V = map(int, input().split())
  for w in range(K, W - 1, -1):
    dp[w] = max(dp[w], dp[w - W]+ V)

print(dp[K])


