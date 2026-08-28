from collections import deque

def solution(arr):
    stk = []
    N = len(arr)
    stk.append(arr[0])
    q = deque(arr)
    
    for i in range(1, N):
        
        if not stk or stk[-1] != arr[i]:
            stk.append(arr[i])
            
        else:
            q.popleft()
        
    return stk
    