def sum_func(n):
  ret = 0
  for i in range(1, n + 1):
    ret += i
  return ret

def sum_by_recur(n):
  if n == 1:
    return 1
  return sum_by_recur(n - 1) + n