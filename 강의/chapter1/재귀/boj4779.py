import sys
input = sys.stdin.readline

N = int(input())
arr = ['-']*(3**N)

def recursive_cantor(my_arr, start, length):
    # idea : 3등분해서 2번째 등분은 전부 ' '로 바꾸고 남은 부분에 대해 재귀때리기
    if length == 1:
        return
    
    partition = length // 3
    
    for i in range(start + partition, start + 2 * partition):
        my_arr[i] = ' '
        
    recursive_cantor(my_arr, start, partition)
    recursive_cantor(my_arr, start + 2*partition, partition)

recursive_cantor(arr, 0, len(arr))

print(''.join(arr))
    
    
        