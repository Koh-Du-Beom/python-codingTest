import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

start = A[-1]
end = sum(A)

while start <= end:
    middle = (start + end) // 2
    sum = 0
    count = 0
    for i in range(N):
        if sum + A[i] > middle:
            count += 1
            sum = 0
        sum += A[i] #앞에서부터 더하면서, 블루레이 크기만큼 채우기
    if sum != 0:
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1
        
print(start)