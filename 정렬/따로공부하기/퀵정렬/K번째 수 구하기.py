import sys
input = sys.stdin.readline

N, K = map(int, input().split())

numbers = list(map(int, input().split()))

def quickSort(start, end, K):
  global numbers
  if start < end:
    pass
  
def cal_pivot(start, end):
  global numbers
  
  if start + 1 == end:
    if numbers[start] > numbers[end]:
      numbers[end], numbers[start] = numbers[start], numbers[end]
    
    middle = (start + end) // 2
    middle, start = start, middle
    pivot = numbers[start]
    i = start + 1
    j = end
    
  while(i <= j):
    while pivot < numbers[i] and j>0:
      j = j - 1
    while pivot > numbers[i] and i < len(numbers) - 1:
      i = i + 1
    if i<=j:
      j, i = i, j
      i += 1
      j -= 1
  
  numbers[start] = numbers[j]
  numbers[j] = pivot
  return j 

quickSort(0, N - 1, K - 1)   
print(numbers[K - 1])  