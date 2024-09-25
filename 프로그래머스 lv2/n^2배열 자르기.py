def solution(n, left, right):
    #한칸한칸 전부 수를 매겨서 하는건 사실상 불가능 
    answer = []
    basic_list = [x for x in range(1, n + 1)] #1,2,3,..., n
    start_point = left // n
    end_point = right // n
    answer_length = right - left + 1
    for i in range(start_point, end_point + 1):
        tmp_list = [i+1] * (i+1) + basic_list[i+1:]
        answer += tmp_list
    
    
    return answer[left % n : left % n + answer_length]