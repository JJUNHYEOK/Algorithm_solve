from collections import deque

def solution(arr):
    q = deque(arr)
    stk = []

    for i in range(len(arr)):
        cur = q.popleft()

        if not stk:
            stk.append(cur)

        else:
            if stk[-1] != cur:
                stk.append(cur)

    return stk    