import sys
input = sys.stdin.readline

N = int(input())
stairs = [0]  # 시작 지점 추가
for _ in range(N):
	stairs.append(int(input()))

# DP 배열 초기화
dp = [0] * (N + 1)

# 초기값 설정
dp[1] = stairs[1]
if N >= 2:
	dp[2] = stairs[1] + stairs[2]

for i in range(3, N + 1):
	dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[N])