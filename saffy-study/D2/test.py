import sys
input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]

for num in num_list:
  a, b = num // 10, num % 10
  print(a + b)