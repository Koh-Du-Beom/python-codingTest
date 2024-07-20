import sys
input = sys.stdin.readline

def recursive_combination(index, level):
  global N, lst, choose
  
  if level == 6:
    for c in choose:
      print(c, end=" ")
    print()
    return
  
  for i in range(index, N):
    choose.append(lst[i])
    recursive_combination(index + 1, level + 1)
    choose.pop()
  


while(True):
  question = list(map(int,input().split()))
  
  N, lst = question[0], question[1:]
  if N == 0:
    break
  
  choose = []
  recursive_combination(0, 0)
  print()
  