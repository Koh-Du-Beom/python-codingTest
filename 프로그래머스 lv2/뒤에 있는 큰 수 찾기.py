import sys
input = sys.stdin.readline

def solution(numbers):
  answer = []
  N = len(numbers)
  
  for i in range(N - 1):
    for j in range(i + 1, N):
      if numbers[i] < numbers[j]:
        answer.append(numbers[j])
        break
    
    if i != len(answer) - 1:
      answer.append(-1)
  
  answer.append(-1)
  return answer


print(solution([9,1,5,3,6,2]))