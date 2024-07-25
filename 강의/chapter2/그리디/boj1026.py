import sys

input = sys.stdin.readline
N = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

result = 0
lst1.sort()
sorted_lst2 = sorted(lst2, key=lambda x: -x)


for i in range(N):
    result += lst1[i] * sorted_lst2[i]

print(result)


