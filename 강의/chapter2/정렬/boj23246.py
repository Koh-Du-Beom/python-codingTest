import sys
input = sys.stdin.readline

N = int(input())

athelete_list = []

for i in range(N):
  athelete_info = list(map(int, input().split()))
  sum_values = sum(athelete_info[1:])
  mul = 1
  for j in range(1, len(athelete_info)):
    mul *= athelete_info[j]
  
  athelete_list.append((athelete_info[0], sum_values, mul))

result = sorted(athelete_list, key=lambda x: (x[2], x[1], x[0]))

for i in range(3):
  print(result[i][0], end=" ")
  


  