import sys
from itertools import permutations

input = sys.stdin.readline

question = input().strip()

def fact(x):
  if x == 0:
    return 1
  return fact(x-1) * x

def is_valid(permutation):
	for i in range(len(permutation) - 1):
		if permutation[i] == permutation[i + 1]:
			return False
	return True

cnt = 0
for permutation in permutations(question):
  if is_valid(permutation):
    cnt += 1
  
for i in range(ord('a'), ord('z') + 1):
  cnt //= fact(question.count(chr(i))) #중복된 것, 예를 들어 abababa가 이 작업이 없으면 다른 것으로 취급되어 cnt가 144가 나옴.
  
  
print(cnt)