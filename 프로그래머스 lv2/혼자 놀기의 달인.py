def solution(cards):
    i = 0 #반복을위한 변수
    answer_list = []
    while(i < len(cards)):
        temp_list = []
        while(True):
            if (i+1) in temp_list:
                answer_list.append(temp_list)
                break
            temp_list.append(cards[i])
            i = cards[i] - 1
        i += 1
        
    print(answer_list)
    
    answer = 0
    return answer

print(solution([8,6,3,7,2,5,1,4]))