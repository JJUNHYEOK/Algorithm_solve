import heapq

def solution(jobs):
    i = 0
    cnt = 0
    cur = 0
    ans = 0
    val = 0
    N = len(jobs)
    queue = []

    jobs.sort()

    while cnt < N:
        while i < N and jobs[i][0] <= cur:
            heapq.heappush(queue, (jobs[i][1], jobs[i][0]))
            i += 1

        if queue:
            dur, start = heapq.heappop(queue)
            cur += dur
            val += (cur - start)
            cnt += 1

        else:
            cur = jobs[i][0]

    ans = val // N

    return ans