def search(lev):
  global N, S, arr, choose, ans
  
  if lev == N:
    if choose and sum(choose):
      ans+= 1
    return
  
  #index가 lev인 원소 선택 o
  choose.append(arr[lev])
  search(lev + 1)
  choose.pop()
  
  # 인덱스가 lev인 원소 선택 x
  search(lev + 1)
  


N, S = map(int, input().split())
arr = list(map(int, input().split()))
choose = []
ans = 0

search(0)

print(ans)