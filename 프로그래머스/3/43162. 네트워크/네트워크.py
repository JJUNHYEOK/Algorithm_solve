from collections import deque

def solution(n, computers):
    visited = [False]*n
    cnt = 0

    def bfs(start):
        q = deque()
        q.append((start))
        visited[start] = True

        while q:
            cur = q.popleft()

            for i in range(n):
                if not visited[i] and computers[cur][i] == 1:
                    q.append((i))
                    visited[i] = True

    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1

    return cnt
