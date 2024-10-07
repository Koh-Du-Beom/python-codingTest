def solution(cards):
    visited = [False] * len(cards)  # 상자의 방문 여부를 체크할 리스트
    answer_list = []
    
    for i in range(len(cards)):
        if not visited[i]:  # 이미 탐색한 상자는 건너뜀
            temp_list = []
            j = i
            
            # 상자를 열어가며 그룹을 형성
            while not visited[j]:
                temp_list.append(cards[j])
                visited[j] = True  # 해당 상자를 열었음을 표시
                j = cards[j] - 1  # 다음 상자의 인덱스
                
            # 그룹의 크기를 저장
            answer_list.append(len(temp_list))
    
    # 그룹 크기를 내림차순으로 정렬
    answer_list.sort(reverse=True)
    
    # 그룹이 2개 이상인 경우 최대 점수 계산
    if len(answer_list) > 1:
        return answer_list[0] * answer_list[1]
    else:
        return 0  # 그룹이 1개 이하인 경우 0점
