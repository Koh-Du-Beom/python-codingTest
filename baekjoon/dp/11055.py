
N = int(input())
numbers = list(map(int, input().split()))

dp = numbers[:]

for i in range(N):
  for j in range(i):
    if numbers[i] > numbers[j]:
      dp[i] = max(dp[i], dp[i] + numbers[j])

print(max(dp))

