import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
  numbers.append(int(input()))

stack = []
num = 1
result = True
answer = ''

for i in range(N):
  su = numbers[i]
  if su >= num:
    while su >= num:
      stack.append(num)
      num += 1
      answer += "+\n"
    stack.pop()
    answer += '-\n'
  else:
    n = stack.pop()
    if n < su:
      print('No')
      result = False
      break
    else:
      answer += '-\n'

if result:
  print(answer)