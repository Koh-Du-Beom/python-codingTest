import sys
input = sys.stdin.readline

N = int(input())
ans = []

for _ in range(N):
  string = list(input().rstrip())
  str_len = len(string)
  flag = 0
  for i in range(str_len // 2):
    left = i
    right = str_len - left - 1
    if string[left] != string[right]:
      if flag == True:
        flag += 1
        break
      
      if flag == False : 
        #문자 삭제하기
        
        flag += 1
        
  ans.append(flag)

for a in ans:
  print(a)
      
    
    
      
      