import sys
input = sys.stdin.readline

N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

# 버블 정렬 알고리즘
for i in range(N):
    change = False
    for j in range(0, N - i - 1):  # 올바른 인덱스 범위 설정
      if numbers[j] > numbers[j + 1]:
        change = True
        numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
    if not change:
      print(i+1)
      break
