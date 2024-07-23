import sys
from itertools import combinations
input = sys.stdin.readline

N, S = map(int, input().split())
lst = list(map(int, input().split()))

cnt = 0

for i in range(1, N):
  for j in combinations(lst, i):
    print(j, sum(j))
    if sum(j) == S:
      cnt += 1
      
print(cnt)