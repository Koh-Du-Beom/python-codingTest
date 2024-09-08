from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for key, value in counter.items():
        if value >= 2:
            answer += value * (value - 1) // 2
            
    weights = set(weights)
    
    for weight in weights:
        if weight * 2 / 3 in weights:
            answer += counter[weight * 2 / 3] * counter[weight]
        if weight * 2 / 4 in weights:
            answer += counter[weight * 2 / 4] * counter[weight]
        if weight * 3 / 4 in weights:
            answer += counter[weight * 3 / 4] * counter[weight]
    
    return answer
  
#다른 풀이
from itertools import combinations
from collections import Counter

def solution(weights):
  cnt = 0
  weights = Counter(weights)
  for a, b in combinations(weights.keys(), 2):
    if a * 2 == b * 3 or a * 2 == b * 4 or a * 3 == b * 4 or b*2 == a*3 or b*2 == a*4 or b*3 == a*4:
      cnt += weights[a] * weights[b]
    
    for v in weights.values():
      if v > 1:
        cnt += sum([i for i in range(1, v)])
  
  return cnt