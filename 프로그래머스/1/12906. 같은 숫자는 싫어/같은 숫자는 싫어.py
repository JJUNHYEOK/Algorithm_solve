from collections import deque

def solution(arr):
    stk = []
    n = len(arr)
    q = deque(arr)

    for i in range(n):
        cur = q.popleft()

        if not stk:
            stk.append(cur)

        else:
            if stk[-1] != cur:
                stk.append(cur)

    return stk
    