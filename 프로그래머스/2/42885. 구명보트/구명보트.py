from collections import deque

def solution(people, limit):
    people.sort()
    q = deque(people)
    cnt = 0
    
    while q:
        heavy = q.pop()
        
        if q:
            if heavy + q[0] <= limit:
                q.popleft()
            
        cnt += 1
                
    return cnt
                