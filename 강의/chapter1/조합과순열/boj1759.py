import sys
input = sys.stdin.readline

dict = ['a', 'e', 'i', 'o', 'u'] #모음이 가능한 조합
choose = []

def is_possible():
  global lv, N, choose, arr
  
  d = 0
  for c in choose:
    d += (c in dict)
  con = lv - d
  
  return (d >= 1 and con >= 2)

def combination(index, level):
  global lv, N, choose, arr
  if level == lv:
    if is_possible():
      print(''.join(choose))
    return
  
  for i in range(index, N):
    choose.append(arr[i])
    combination(i + 1, level + 1)
    choose.pop()
    
    
lv, N = map(int, input().split())
arr = input().split()

arr.sort()
combination(0, 0)
    
  
    
  
    
  