from collections import deque

def solution(n, computers):

    visited = [False]*(n+1)

    def bfs(start):
        visited[start] = True
        q = deque()
        q.append(start)

        while q:
            cur = q.popleft()

            for i in range(n):
                if not visited[i] and computers[cur][i] == 1:
                    q.append(i)
                    visited[i] = True
    cnt = 0

    for i in range(n):
        if not visited[i]:
            bfs(i)
            cnt += 1

    return cnt
