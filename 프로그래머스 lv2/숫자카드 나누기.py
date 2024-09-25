from math import gcd
from functools import reduce

def get_gcd(numbers):
    return reduce(gcd, numbers)

def not_div(array, gcd):
    for arr in array:
        if arr % gcd == 0:
            return False
    
    return True

def solution(arrayA, arrayB):
    answer = 0
    gcd_a = get_gcd(arrayA)
    gcd_b = get_gcd(arrayB)
    
    if not_div(arrayA, gcd_b):
        answer = max(answer, gcd_b)
    
    if not_div(arrayB, gcd_a):
        answer = max(answer, gcd_a)
    
    return answer