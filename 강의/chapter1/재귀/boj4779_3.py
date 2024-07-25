#강사풀이2

def function(k):
    #종료조건
    if k == 0:
        return '-'
    
    #재귀
    return function(k-1) + (' ' * (3 ** (k-1))) + function(k-1)

while True:
    try:
        N = int(input())
        print(function(N))
    except:
        break