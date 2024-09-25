from queue import PriorityQueue

INF = int(1e12)
MAX = int(1e6)

def solution(x, y, n):
    #다익스트라
    pq = PriorityQueue()
    time = [INF] * (MAX + 1)
    time[x] = 0
    pq.put([0, x])
    
    while not pq.empty():
        cur_time, cur_pos = pq.get()
        
        nexts = [
            (cur_time + 1, cur_pos + n),
            (cur_time + 1, cur_pos * 2),
            (cur_time + 1, cur_pos * 3),
        ]
        
        for next_time, next_pos in nexts:
            if 0 <= next_pos <= MAX:
                if next_time < time[next_pos]:
                    time[next_pos] = next_time
                    pq.put([next_time, next_pos])
    
    if time[y] == INF:
        return -1
    else:
        return time[y]


#다른 풀이
def solution(x, y, n):
  answer = 0
  s = set()
  s.add(x)
  
  while s:
    if y in s:
      return answer
    
    nxt = set()
    for i in s:
      if i + n <= y:
        nxt.add(i + n)
      if i * 2 <= y:
        nxt.add(i * 2)
      if i * 3 <= y:
        nxt.add(i * 3)
    
    s = nxt
    answer += 1
  
  return -1