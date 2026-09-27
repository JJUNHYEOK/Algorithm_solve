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

# ##########################
# ##########################

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    dist = [[-1]*m for _ in range(n)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        dist[x][y] = 1

        while q:
            xx, yy = q.popleft()

            for d in range(4):
                nx = xx + dr[d]
                ny = yy + dc[d]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        dist[nx][ny] = dist[xx][yy] + 1

                        if nx == n-1 and ny == m-1:
                            return True

        return False

    if bfs(0, 0):
        return dist[n-1][m-1]

    return -1