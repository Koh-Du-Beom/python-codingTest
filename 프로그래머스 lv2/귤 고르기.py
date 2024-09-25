from collections import Counter

def solution(k, tangerine):
    result = 0; answer = 0
    
    counter = Counter(tangerine) # 카운터 선언
    counter = counter.most_common()
    
    print(counter)
    
    for key, value in counter:
        result += value
        answer += 1
        if result >= k:
            return answer
        
    
print(solution(6, [1,3,2,5,4,5,2,3]))
   
