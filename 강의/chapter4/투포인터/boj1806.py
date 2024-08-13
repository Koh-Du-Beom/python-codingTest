import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

ans = int(1e12)
right = -1
cur_sum = 0
for left in range(N):
  while right + 1 < N and cur_sum + arr[right + 1] < M:
    right += 1
    cur_sum += arr[right]
    
  if cur_sum < M and right + 1 < N:
    right += 1
    cur_sum += arr[right]
  
  if right < N and cur_sum >= M:
    ans = min(ans, right - left + 1)

  cur_sum -= arr[left]

print(ans if ans != int(1e12) else 0)
