#백준 11399번
import sys
input = sys.stdin.readline

N = int(input())
S = [0] * N

numbers = list(map(int, input().split(' ')))
print(numbers)
for i in range(1, N):
  insert_point = i
  insert_value = numbers[i]
  for j in range(i-1, -1, -1):
    if numbers[j] < numbers[i]:
      insert_point = j + 1
      break
    if j == 0:
      insert_point = 0
  
  for j in range(i, insert_point, -1):
    numbers[j] = numbers[j-1]
  numbers[insert_point] = insert_value

S[0] = numbers[0]
for i in range(1, N):
  S[i] = S[i-1] + numbers[i]

sum = 0

for s in S:
  sum += s

print(sum)
    