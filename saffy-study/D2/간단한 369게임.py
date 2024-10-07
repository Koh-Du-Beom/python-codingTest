import sys
input = sys.stdin.readline

def check_three(number):
  number = str(number)
  count = 0
  for num in number:
    if num == '3' or num == '6' or num == '9':
      count += 1
  
  return '-' * count

N = int(input())
for i in range(1, N + 1):
  if check_three(i):
    print(check_three(i), end=" ")
  print(i, end = " ")


  
