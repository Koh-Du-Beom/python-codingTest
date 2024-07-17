import sys
input = sys.stdin.readline

N = int(input())

count = 1 #연속된 자연수합의 set이 몇개인지 개수 저장
start = 1; end = 1; sum = 1; #시작점, 끝점, 합을 저장
    
while(end != N):
  if sum == N:
    count += 1
    end += 1
    start += end
  elif sum > N:
    sum -= start
    start += 1
  else:
    end += 1
    start += end
    
print(count)
    