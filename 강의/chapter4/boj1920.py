import sys
input = sys.stdin.readline

def binary_search(x):
    global origin_list
    start = 0
    end = len(origin_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if origin_list[mid] > x:
            end = mid - 1
        elif origin_list[mid] < x:
            start = mid + 1
        else:
            return True
    return False

N = int(input())
origin_list = list(map(int, input().split()))
origin_list = sorted(origin_list)

M = int(input())
check_list = list(map(int, input().split()))

for check in check_list:
    if binary_search(check):
        print(1)
    else:
        print(0)
