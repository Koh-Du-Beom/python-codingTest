import sys
input = sys.stdin.readline

# def solution(numbers):
#   answer = []
#   N = len(numbers)
  
#   for i in range(N - 1):
#     for j in range(i + 1, N):
#       if numbers[i] < numbers[j]:
#         answer.append(numbers[j])
#         break
    
#     if i != len(answer) - 1:
#       answer.append(-1)
  
#   answer.append(-1)
#   return answer
# 시간초과가 나는 풀이. 일반적으로 순회하며 풀면 안된다.

def solution(numbers):
  stack = []
  answer = [-1] * len(numbers)
  
  for i in range(len(numbers)):
    while stack and numbers[stack[-1]] < numbers[i]:
      answer[stack.pop()] = numbers[i]
    stack.append(i)
  
  return answer

#스택에 인덱스를 담아가면서 number[i]가 즉, 최신의 원소가 스택에 담아둔
#요소보다 클때까지 계속 pop하면서 answer에 저장함.
