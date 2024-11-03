from collections import Counter

T = int(input())

for _ in range(T):
	test_case_number = int(input())
	numbers = []
	while len(numbers) < 1000:
			numbers.extend(map(int, input().split()))
	counter = Counter(numbers)
	most_common = counter.most_common()
	max_count = most_common[0][1]
	modes = [num for num, cnt in most_common if cnt == max_count]
	mode = max(modes)  # 최빈값이 여러 개일 경우 가장 큰 값을 선택
	print('#{} {}'.format(test_case_number, mode))
