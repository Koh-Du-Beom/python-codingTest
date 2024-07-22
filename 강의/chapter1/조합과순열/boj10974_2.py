from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())

for permutation in permutations(range(1, N+1)):
  print(' '.join(map(str, permutation)))
  
  