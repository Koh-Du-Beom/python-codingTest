import sys
input = sys.stdin.readline

N = int(input())

result = 0
numbers = list(map(int, input().split()))
numbers.sort()

for k in range(N):
  find = numbers[k]
  i = 0
  j = N - 1
  while i < j:
    if numbers[i] + numbers[j] == find:
      if i!=k and j!=k:
        result += 1
        break
      elif i == k:
        i += 1
      elif j == k:
        j -= 1
    elif numbers[i] + numbers[j] < find :
      i += 1
    else:
      j -= 1