import sys
input = sys.stdin.readline
from collections import deque

N, L = map(int, input().split())
mydeque = deque()
numbers = list(map(int, input().split()))

for i in range(N):
  while mydeque and mydeque[-1][0] > numbers[i]:
    mydeque.pop()
  mydeque.append(numbers[i], i)
  if mydeque[0][1] <= i - L:
    mydeque.popleft()
  print(mydeque[0][0], end='')
