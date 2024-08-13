import sys
input = sys.stdin.readline

def is_palindrome(s):
  for left in range(len(s)):
    right = len(s) - left - 1
    if s[left] != s[right]:
      return False
  return True

def is_pseudo_palindrome(s):
	for left in range(len(s)):
		right = len(s) - left - 1
		if s[left] != s[right]:
			s1 = s[:left] + s[left + 1:]
			s2 = s[:right] + s[right + 1:]
			if is_palindrome(s1) or is_palindrome(s2):
				return True
			else:
				return False


def solve():
  S = input().rstrip()
  
  if is_palindrome(S):
    print(0)
    return
  
  if is_pseudo_palindrome(S):
    print(1)
    return
  
  print(2)

N = int(input())

for _ in range(N):
  solve()


