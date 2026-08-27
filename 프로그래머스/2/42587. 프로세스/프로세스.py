from collections import deque

def solution(priorites, location):

    q = deque()
    n = len(priorites)

    for i in range(n):
        q.append((i, priorites[i]))

    order = 0

    while q:
        cur_idx, cur_val = q.popleft()

        for item in q:
            if item[1] > cur_val:
                q.append((cur_idx, cur_val))
                break

        else:
            order += 1

            if cur_idx == location:
                return order