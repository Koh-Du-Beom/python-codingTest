#따로해보기

import sys
input = sys.stdin.readline

N = int(input())
numbers = []

for i in range(N):
  numbers.append(int(input()))
  
def mergeSort(start, end):
  if end - start <  1:
    return
  
  middle = (start + end) // 2 
  
  mergeSort(start, middle)
  mergeSort(middle+1, end)
  
  for i in range(start, end + 1):
    pass