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
                for j in range(len(q)):
                    q[j] = -q[j]

                heapq.heapify(q)
                heapq.heappop(q)

                for j in range(len(q)):
                    q[j] = -q[j]

                heapq.heapify(q)

    if not q:
        return [0, 0]

    return [max(q), min(q)]