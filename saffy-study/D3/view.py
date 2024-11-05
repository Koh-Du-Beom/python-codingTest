
for test in range(1, 10 + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0 
    for i in range(2, N-2):
        left_obstacle = max(buildings[i-2], buildings[i-1]); left_result = 0 #왼쪽 옆 건물 조사
        if left_obstacle < buildings[i]:
            left_result = buildings[i] - left_obstacle
            
        right_obstacle = max(buildings[i+1], buildings[i+2]); right_result = 0
        if right_obstacle < buildings[i]:
            right_result = buildings[i] - right_obstacle
            
        result += min(right_result, left_result)
    
    print('#{} {}'.format(test, result))
        