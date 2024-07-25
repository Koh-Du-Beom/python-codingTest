import sys
input = sys.stdin.readline

N, M = map(int, input().split())
positive = []; negative = []

max_num = 0
numbers = list(map(int, input().split()))
for num in numbers:
    if abs(max_num) < abs(num):
        max_num = abs(num) #절댓값이 가장 큰 지점은 마지막에 방문한것으로 취급할건데
        #그 값을 알아내서 왕복한것으로 모두 계산하고 한번 빼주는 형식으로 할 것임.
        
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)
        
negative = sorted(negative)
positive = sorted(positive, reverse=True)

print(negative, positive)

result = 0
for i in range(0, len(negative), M):
    result += 2 * abs(negative[i])  #음수처리
    
for i in range(0, len(positive), M):
    print(positive[i])
    result += 2 * abs(positive[i])

print(result - max_num)


    
    


    

