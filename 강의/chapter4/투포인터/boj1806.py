import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

ans_len = N + 1
right = -1

cur_sum = 0
for left in range(N):
  cur_len = 0
  while right + 1 < N and cur_sum + arr[right + 1] <= M:
    right += 1
    cur_sum += arr[right]
    cur_len += 1
  
  if cur_sum == M:
    ans_len = cur_len
  
  cur_sum -= arr[left]

print(ans_len)