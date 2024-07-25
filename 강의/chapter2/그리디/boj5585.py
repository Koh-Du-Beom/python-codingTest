import sys
input = sys.stdin.readline

N = int(input())
change = 1000 - N

count = 0


count += change // 500
change %= 500

count += change // 100
change %= 100

count += change // 50
change %= 50

count += change // 10
change %= 10

count += change // 5
change %= 5

count += change

print(count)
    