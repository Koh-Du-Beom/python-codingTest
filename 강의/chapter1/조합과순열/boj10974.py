import sys
input = sys.stdin.readline

def recursive_permutation(level):
  global N, choose, check
  if level == N:
    print(' '.join(map(str, choose)))
    return
  
  for i in range(1, N+1):
    if check[i] == True:
      continue
    
    choose.append(i)
    check[i] = True
    
    recursive_permutation(level + 1)
    
    check[i] = False
    choose.pop()    

N = int(input())
choose = []
check = [False] * (N+1)

recursive_permutation(0)