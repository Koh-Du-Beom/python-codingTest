import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
  numbers.append((int(input()), i))


MAX = 0
sorted_numbers = sorted(numbers)
print(sorted_numbers)

for i in range(N):
  if MAX < sorted_numbers[i][1] - i:
    MAX = sorted_numbers[i][1] - i

print(MAX + 1)
# for i in range(N):
#     change = False
#     for j in range(0, N - i - 1): 
#       if numbers[j] > numbers[j + 1]:
#         change = True
#         numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
#     if not change:
#       print(i+1)
#       break
    
#이대로 풀면 시간초과

