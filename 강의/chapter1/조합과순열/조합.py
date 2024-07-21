
N = 10
R = 5
lst = [1,2,3,4,5,6,7,8,9,10]
choose = []

def combination(index, level):
  if level == R:
    #level이 R이면 전부 선택한 것이므로 종료
    print(choose)
    return

  for i in range(index, N):
    choose.append(lst[i])
    combination(i+1, level+1)
    choose.pop()

combination(0, 0)
#index : 이전에 선택한 원소 인덱스 + 1
#level : 현재 선택한 원소의 개수