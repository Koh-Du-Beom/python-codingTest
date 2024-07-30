import sys
input = sys.stdin.readline

start_black_board = [
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
]

start_white_board = [
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
    ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
    ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
]

def get_min(i, j):
    global new_chess_board, start_black_board, start_white_board
    case1 = case2 = 0
    for x in range(8):
        for y in range(8):
            case1 += (new_chess_board[x+ i][y+ j] != start_black_board[x][y])
            case2 += (new_chess_board[x+ i][y+ j] != start_white_board[x][y])
    
    return min(case1, case2)

N, M = map(int, input().split())
new_chess_board = []
for i in range(N):
    new_chess_board.append(input())

best = 1e12 #몇개 바꾸는지 최솟값 변수. 처음엔 매우 큰 값
for j in range(M):
    for i in range(N):
        if i + 7 >= N or j + 7 >= M:
            continue
        best = min(best, get_min(i, j))
    
print(best)    

    
