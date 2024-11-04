from itertools import combinations

T = int(input())

for test in range(1, T + 1):
    N, R = map(int, input().split())
    print('#{} {}'.format(test, len(combinations(N,R))))
    