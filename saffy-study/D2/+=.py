def fibo(A, B, limit):  # 변수명 N -> limit으로 변경하여 전역 변수 N과 충돌 방지
    fib = [0, 0]
    fib[0] = A; fib[1] = B
    fib.sort()
    idx = 0
    count = 0
    while True:
        new_value = fib[0] + fib[1]  # 피보나치 수열을 계산하여 새로운 값을 생성
        fib[idx] = new_value  # fib 리스트의 idx 위치에 새로운 값 저장
        idx = (idx + 1) % 2  # 0과 1 사이에서 인덱스를 번갈아가며 사용
        count += 1
        
        if new_value > limit:  # limit을 넘어서는 순간 count 반환
            return count

test_cases = int(input())  # 입력받은 N을 반복 횟수로 사용

for _ in range(test_cases):
    A, B, limit = map(int, input().split())  # N -> limit으로 변경
    print(fibo(A, B, limit))
