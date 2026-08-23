from collections import deque

def solution(priorities, location):
    q = deque(enumerate(priorities))

    sorted_process = sorted(priorities, reverse=True)

    order = 0
    max_idx = 0

    while q:
        idx, priority = q.popleft()

        if priority == sorted_process[max_idx]:
            order += 1
            max_idx += 1

            if idx == location:
                return order

        else:
            q.append((idx, priority))