import sys
input = sys.stdin.readline

N = int(input())

stack = []
numbers = list(map(int, input().split()))
answer = [0] * N

for i in range(N):
	while stack and numbers[stack[-1]] < numbers[i]:
		answer[stack.pop()] = numbers[i]
  
 stack.append(i)

while stack:
  answer[stack.pop()] = -1
  
result = ''
for i in range(N):
  result += str(answer[i]) + ''

print(result)
  