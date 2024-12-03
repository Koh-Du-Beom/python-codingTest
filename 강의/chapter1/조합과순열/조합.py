from itertools import combinations
import sys
input = sys.stdin.readline


while True:
  choose = []
  now_input = list(map(int, input().split()))
  N, arr = now_input[0], now_input[1 : ]
  
  if N == 0:
    break

  for comb in combinations(arr, 6):
    for u in comb:
      print(u, end = " ")
    print()
  print()