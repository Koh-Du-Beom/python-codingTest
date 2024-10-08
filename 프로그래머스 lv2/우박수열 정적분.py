
def solution(k, ranges):
    numbers = []
    numbers.append(k)
    while (k > 1):
        if k % 2 == 0:
            k /= 2
            numbers.append(k)
        else:
            k = k * 3 + 1
            numbers.append(k)
    
    #numbers배열에 구간을 정의
    n = len(numbers) - 1
    answer = []
    for a, b in ranges:
        start = a; end = n + b
        print(a, b)
        print(start, end)
        if start > end:
            answer.append(-1.0)
            continue
            
        if start == end:
            answer.append(0.0)
            continue
            
        
        result = (numbers[start] + numbers[end]) / 2 + sum(numbers[start + 1 : end])
        answer.append(result)
    
    return answer
  
print(solution(5, [[0,0],[0,-1],[2,-3],[3,-3]]))