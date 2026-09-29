import heapq

def solution(operations):

    q = []

    for i in range(len(operations)):
        cmd, val = operations[i].split()
        val = int(val)

        if cmd == 'I':
            heapq.heappush(q, val)

        if cmd == 'D' and val == -1:
            if q:
                heapq.heappop(q)

        if cmd == 'D' and val == 1:
            if q:
                max_val = max(q)
                q.remove(max_val)
                heapq.heapify(q)

    if not q:
        return [0, 0]

    return [max(q), min(q)]