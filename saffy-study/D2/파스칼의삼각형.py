def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def combination(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

T = int(input())
for _ in range(T):
    N = int(input())
    print('#{}'.format(T))
    for i in range(0, N):
        for j in range(0, i + 1):
            print(combination(i, j), end=" ")
        print()