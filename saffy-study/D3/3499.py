
T = int(input())

for test in range(1, T + 1):
    N = int(input())
    cards = list(input().split(" "))
    
    if N % 2 == 0:
        division = N // 2
        left_cards, right_cards = cards[0 : division], cards[division : N]
    else:
        division = N // 2
        left_cards, right_cards = cards[0 : division + 1], cards[division + 1 : N]
    
    print('#{}'.format(test), end=" ")
    while left_cards and right_cards:
        pop_left = left_cards.pop(0)
        pop_right = right_cards.pop(0)
        print(pop_left, pop_right, end = " ")
        
        
    if left_cards:
        print(left_cards.pop(0))
    
    print()
    
        
    