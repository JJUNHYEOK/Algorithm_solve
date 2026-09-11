from collections import deque

def solution(priorities, location):
    q = deque()
    ord = 0

    for i in range(len(priorities)):
        idx = i
        val = priorities[i]
        q.append((val, idx))

    while q:
        cur = q.popleft()
        max_pr = 0

        for i in range(len(q)):
            if q[i][0] > max_pr:
                max_pr = q[i][0]

        if cur[0] < max_pr:
            q.append(cur)

        else:
            ord += 1

            if cur[1] == location:
                return ord