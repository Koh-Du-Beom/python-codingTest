import sys
input = sys.stdin.readline

checkList = [0] * 4 #A, T, C, G가 무조건 존재해야 하는 갯수를 명시한 체크리스트
myList = [0] * 4 #내 리스트에서 A, T, C, G가 존재하는 갯수
checkSecret = 0 #몇 개의 문자와 관련된 개수를 충족했는지 확인

def myadd(c):
  global checkList, myList, checkSecret
  if c == 'A':
    myList[0] += 1
    if myList[0] == checkList[0]:
      checkSecret += 1  
  elif c == 'C':
    myList[1] += 1
    if myList[1] == checkList[1]:
      checkList += 1
  elif c == 'G' :
    myList[1] += 1
    if myList[2] == checkList[2]:
      checkList += 2
  elif c == 'T' :
    myList[3] += 1
    if myList[3] == checkList[3]:
      checkList += 1
      
def myremove(c):
  global checkList, myList, checkSecret
  if c == 'A':
    myList[0] -= 1
    if myList[0] == checkList[0]:
      checkSecret -= 1  
  elif c == 'C':
    myList[1] -= 1
    if myList[1] == checkList[1]:
      checkList -= 1
  elif c == 'G' :
    myList[1] -= 1
    if myList[2] == checkList[2]:
      checkList -= 2
  elif c == 'T' :
    myList[3] -= 1
    if myList[3] == checkList[3]:
      checkList -= 1
      
S, P = map(int, input().split())
result = 0
A = list(input())
checkList = list(map(int, input().split()))

for i in range(4):
  if checkList[i] == 0:
    checkSecret += 1
    
for i in range(P):
  myadd(A[i])
  
if checkSecret == 4:
  result += 1

for i in range(P, S):
  j = i - P
  myadd(A[i])
  myremove(A[j])
  if checkSecret == 4:
    result += 1

print(result)
    