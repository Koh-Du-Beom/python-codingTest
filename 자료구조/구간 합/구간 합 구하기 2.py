import sys
input = sys.stdin.readline

N, M = map(int, input().split())

origin_numbers = [[0] * (N + 1)] #원래 숫자를 입력받을 배열
for i in range(N):
  row = [0] + [int(x) for x in input().split()]
  origin_numbers.append(row)

print(origin_numbers)  

prefix_numbers = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N + 1):
  for j in range(1, N + 1):
    prefix_numbers[i][j] = prefix_numbers[i-1][j] + prefix_numbers[i][j-1] + origin_numbers[i][j] - prefix_numbers[i-1][j-1]

for _ in range(M):
  x1, y1, x2, y2 = map(int, input().split())
  result = ( prefix_numbers[x2][y2] - prefix_numbers[x1-1][y2] 
  - prefix_numbers[x2][y1-1] + prefix_numbers[x1-1][y1-1] )
  
  print(result)