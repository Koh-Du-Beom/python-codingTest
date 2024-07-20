N = 10
R = 3
lst = [1,2,3,4,5,6,7,8,9,10]
check = [False]
#check[k]가 true면 인덱스k인 원소를 사용중임을 나타냄
choose = []

def permutation(level):
  if level == R:
    print(choose)
    return
  
  for i in range(0, N):
    if check[i] == True:
      continue
    
    choose.append(lst[i])
    check[i] = True
    permutation(level + 1)
    
    check[i] = False
    choose.pop()