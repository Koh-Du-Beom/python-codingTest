
def solution(elements):
    num_set = set()
    elements_length = len(elements)
    
    elements = elements * 2
    for i in range(elements_length):
        for j in range(elements_length):
            num_set.add(sum(elements[j:j+i]))
    
    answer = len(num_set)
    return answer