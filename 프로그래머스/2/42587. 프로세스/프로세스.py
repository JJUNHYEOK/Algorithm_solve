from collections import deque

def solution(priorities, location):
    
    q = deque()
    
    for i in range(len(priorities)):
        idx = i
        val = priorities[i]
        q.append((val, idx))
        
    order = 0
    
    while q:
        cur = q.popleft()
        
        if q and cur[0] < max(item[0] for item in q):
            q.append(cur)
                
        else:
            order += 1
            if cur[1] == location:
                return order