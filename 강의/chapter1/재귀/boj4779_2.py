#강사풀이

#일정한 패턴이 있음에 착안
#f(0)은 그냥 - 이고 
#f(1)은 f(0) " " f(0)
#f(2)도 마찬가지로 f(1) 형태에 가운데 공백이 있고, f(1)
#이런식으로 반복되는 구조를 생각해보게 된다면 아래와 같은 풀이가 나옴.
ans = ['' for _ in range(13)]
ans[0] = '-'

for i in range(1, 13):
    ans[i] = ans[i-1] + (' ' * (3 ** (i-1))) + ans[i-1]

while(True):
    try:
        N = int(input())
        print(ans(N))
    except:
        break