
def func(lev):
  global S, chars, cnt, choose, ans
  
  if lev == len(S):
    ans += 1
    return
  
  for c in chars:
    if cnt[c] == 0:
      continue
    
    if (not choose) or (choose[-1]) != c: #choose의 마지막이 c와 다른경우
      cnt[c] -= 1
      choose.append(c)
      func(lev + 1)
      cnt[c] += 1
      choose.pop()

S = input()
chars = set()
cnt = dict()

for c in S:  #문자열의 갯수를 세는 작업임.
  chars.add(c)
  if c not in cnt:
    cnt[c] = 0
  cnt[c] += 1

choose = []
ans = 0

func(0)

print(ans)