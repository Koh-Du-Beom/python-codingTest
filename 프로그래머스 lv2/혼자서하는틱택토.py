def solution(board):
    circle_count, x_count = 0, 0
    circle_complete, x_complete = 0, 0  # O와 X가 완성된 경우를 체크
    
    # O와 X의 개수 세기
    for i in range(3):
        for b in board[i]:
            if b == 'O':
                circle_count += 1
            if b == 'X':
                x_count += 1

    # 가로, 세로, 대각선으로 O와 X가 완성된 경우 체크
    for i in range(3):
        if board[i] == 'OOO':  # 가로로 O 완성
            circle_complete += 1
        if board[i] == 'XXX':  # 가로로 X 완성
            x_complete += 1
        if board[0][i] == board[1][i] == board[2][i] == 'O':  # 세로로 O 완성
            circle_complete += 1
        if board[0][i] == board[1][i] == board[2][i] == 'X':  # 세로로 X 완성
            x_complete += 1

    # 대각선 체크
    if board[0][0] == board[1][1] == board[2][2] == 'O':  # 첫 번째 대각선 O 완성
        circle_complete += 1
    if board[0][0] == board[1][1] == board[2][2] == 'X':  # 첫 번째 대각선 X 완성
        x_complete += 1
    if board[0][2] == board[1][1] == board[2][0] == 'O':  # 두 번째 대각선 O 완성
        circle_complete += 1
    if board[0][2] == board[1][1] == board[2][0] == 'X':  # 두 번째 대각선 X 완성
        x_complete += 1
    
    # 규칙 위반 여부 체크
    # 1. O의 개수가 X보다 작으면 안됨
    if circle_count < x_count:
        return 0
    
    # 2. O의 개수와 X의 개수 차이가 2 이상이면 안됨
    if circle_count - x_count > 1:
        return 0
    
    # 3. O가 이겼을 때 X와 O의 개수가 같으면 안됨 (게임이 끝났는데 더 진행됨)
    if circle_complete > 0 and circle_count == x_count:
        return 0
    
    # 4. X가 이겼을 때 X와 O의 개수가 다르면 안됨 (개수가 같아야 정상)
    if x_complete > 0 and circle_count != x_count:
        return 0

    # 5. O와 X가 동시에 이겼으면 안됨
    if circle_complete > 0 and x_complete > 0:
        return 0
    
    return 1
