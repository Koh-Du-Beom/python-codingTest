from math import sqrt

def get_divisors(n):
	s = set()
	for i in range(1, int(sqrt(n)) + 1):
		if n % i == 0:
			s.add(i)
			s.add(n // i)
	return s

def get_GCD(a, b):
  set_a = get_divisors(a)
  set_b = get_divisors(b)
  return max(set_a & set_b)

def get_LCM(a, b):
	return (a * b // get_GCD(a, b))

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a % b)

N = 120
is_prime = [True] * (N + 1)  # 처음에는 모두 true로 초기화
is_prime[1] = False  # 1은 소수가 아니므로

for i in range(2, int(sqrt(N)) + 1):
	if not is_prime[i]: 
		continue
	for j in range(2 * i, N + 1, i):
		is_prime[j] = False

for i in range(1, N + 1):
    print(i, is_prime[i])