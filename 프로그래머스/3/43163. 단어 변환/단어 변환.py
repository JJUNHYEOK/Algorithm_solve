from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0

    q = deque()
    q.append((begin, 0))
    visited = set([begin])

    while q:
        cur, dist = q.popleft()

        if cur == target:
            return dist

        for nxt in words:
            if nxt not in visited:
                cnt = 0

                for i in range(len(cur)):
                    if cur[i] != nxt[i]:
                        cnt += 1

                if cnt == 1:
                    visited.add(nxt)
                    q.append((nxt, dist+1))


    return 0