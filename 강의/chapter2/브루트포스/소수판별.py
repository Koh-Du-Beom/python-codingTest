N = 1000
result = 0

for i in range(1, N+1):
  if i == 1:
    continue
  
  is_prime = True
  
  for j in range(2, i):
    if i % j == 0:
      is_prime = False
      
  if is_prime:
    result += 1