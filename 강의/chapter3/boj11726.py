import sys
input = sys.stdin.readline

def func(n):
  global dp
  
  #base case
  if n == 1 or n == 2:
    return n
  if dp[n] != -1:
    return dp[n]
  
  #recursive case
  dp[n] = (func(n-1) + func(n-2)) % 10007
  return dp[n]
  
  

N = int(input())
dp = [-1 for _ in range(N+1)]
print(func(N))