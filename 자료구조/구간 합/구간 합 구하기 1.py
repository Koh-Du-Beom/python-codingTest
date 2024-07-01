import sys
input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

prefix_sum = [0]
for i in range(N):
  prefix_sum.append(prefix_sum[i] + numbers[i])

for j in range(M):
  start, end = map(int, input().split())
  print(prefix_sum[end] - prefix_sum[start-1])