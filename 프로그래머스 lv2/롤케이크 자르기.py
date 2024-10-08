from collections import Counter

def solution(topping):
    left_set = Counter(topping)
    right_set = { }
    answer = 0
    
    for i in range(len(topping)):
        if topping[i] in right_set:
            right_set[topping[i]] += 1
        else:
            right_set[topping[i]] = 1
    
        left_set[topping[i]] -= 1
        if not left_set[topping[i]]:
            del left_set[topping[i]]
        
        if len(left_set) == len(right_set):
            answer += 1
    
    return answer