import sys
input = sys.stdin.readline
N = int(input())

arr = [-1] * (N+2)
arr[0] = 0
arr[1] = 1

def fibonacci(x):
    global arr
    if arr[x] != -1:
        return arr[x]
    
    arr[x] = fibonacci(x-1) + fibonacci(x-2)
    return arr[x]

print(fibonacci(N))
