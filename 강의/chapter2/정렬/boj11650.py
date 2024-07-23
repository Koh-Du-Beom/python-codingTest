import sys
input = sys.stdin.readline

N = int(input())

coordinates = []
for i in range(N):
  x, y = map(int, input().split())
  coordinates.append((x,y))

result = sorted(coordinates, key=lambda x : (x[0], x[1]))
print(result)