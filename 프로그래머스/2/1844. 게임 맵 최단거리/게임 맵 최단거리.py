from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]

    def bfs(s_x, s_y):
        q = deque()
        q.append((s_x, s_y))
        visited[s_x][s_y] = True
        maps[s_x][s_y] = 1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while q:
            cur_x, cur_y = q.popleft()

            if cur_x == n-1 and cur_y == m-1:
                return maps[cur_x][cur_y]

            for d in range(4):
                nx = cur_x+dx[d]
                ny = cur_y+dy[d]

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if maps[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        maps[nx][ny] = maps[cur_x][cur_y] + 1

        return -1

    return bfs(0,0)
