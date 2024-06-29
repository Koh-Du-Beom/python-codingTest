import sys
input = sys.stdin.readline

numbers = input().strip()
digits = [int(number) for number in numbers]

for i in range(len(digits)):
  max = i
  for j in range(i+1, len(digits)):
    if digits[j] > digits[max]:
      max = j
  
  if digits[max] > digits[i]:
    digits[max], digits[i] = digits[i], digits[max]
  
for i in range(len(digits)):
  print(digits[i], end="")    