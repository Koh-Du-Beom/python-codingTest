import sys
input = sys.stdin.readline

def fibo(n):
  #Base Case
  if n == 0:
    return 0
  
  if n == 1:
    return 1
  
  return fibo(n-1) + fibo(n-2)

N = int(input())
print(fibo(N))