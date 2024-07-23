from math import sqrt

N = 120
is_prime = [True] * (N+1)
is_prime[1] = False

for i in range(2, int(sqrt(N)) + 1):
  if not is_prime[i]:
    continue
  for j in range(2*i, N+1, i): #배수를 소수가 아닌것으로 처리하는 부분
    is_prime[j] = False

for i in range(1, N+1):
  print(i, is_prime[i])