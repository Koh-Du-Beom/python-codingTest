import sys
input = sys.stdin.readline

N, M = map(int, input().split())
origin_numbers = list(map(int, input().split()))

prefix_numbers = [0] * (N+1)
for i in range(1, N+1):
  prefix_numbers[i] = prefix_numbers[i-1] + origin_numbers[i-1]

mod_numbers = prefix_numbers[1:]

count_numbers = [0]*(M-1)
answer = 0
for i in range(0, N):
  remainder = mod_numbers[i] % M 
  if remainder == 0:
    answer += 1
  count_numbers[remainder] += 1
  

for i in range(M-1):
  if count_numbers[i] > 1:
    answer += (count_numbers[i] * (count_numbers[i] - 1) // 2) 
  
print(answer)