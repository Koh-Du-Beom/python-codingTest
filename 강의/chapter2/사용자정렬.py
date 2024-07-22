def comp(x):
  return -x

arr1 = [4,2,3,1,5]
print(sorted(arr1))
print(sorted(arr1, key=comp))
print(sorted(arr1, key=lambda x: -x))
print(sorted(arr1, key=lambda x: x))

lst = [(3,10), (4,20), (1, 30), (2, 20)]
result = sorted(lst, key=lambda x: (-x[1], x[0]))
print(result)
