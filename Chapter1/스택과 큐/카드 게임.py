import sys
input = sys.stdin.readline

N = int(input())

numbers = [x for x in range(1, N+1)]

while(len(numbers) > 1):
  numbers.pop(0)
  back_num = numbers.pop(0)
  numbers.append(back_num)
  

print(numbers[0])