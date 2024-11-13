
def transpose_arr(arr):
  copy_arr = arr
  for i in range(len(copy_arr)):
    for j in range(len(copy_arr)):
      copy_arr[i][j], copy_arr[j][i] = copy_arr[j][i], copy_arr[i][j]

  return copy_arr

def cal_diagonal(arr):
  diagonal_sum = 0
  for i in range(len(arr)):
    diagonal_sum += arr[i][i]
  
  return diagonal_sum

T = int(input())
for test in range(1, T + 1):
  matrix = [list(map(int, input().split())) for _ in range(100)]
  sum_array = []
  for mat in matrix:
    sum_array.append(sum(mat)) #가로 더하기 연산
  
  transpose_matrix = transpose_arr(matrix)

  for mat in transpose_matrix:
    sum_array.append(sum(mat))

  diagnoal_sum = cal_diagonal(matrix)
  sum_array.append(diagnoal_sum)

  print('#{} {}'.format(test, max(sum_array)))