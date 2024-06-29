import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
  numbers.append(int(input()))
  
for i in range(N-1, 1, -1):
  for j in range(i):
    if numbers[j] > numbers[j+1]:
      numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
  
  print(numbers)
    
    
print(numbers)