from collections import deque

def solution(maps):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps)
    m = len(maps[0])    

    def bfs(x, y):
        q = deque([(x, y)]) # deque 형태 기억하기
        maps[x][y] = 1

        while q:
            a, b = q.popleft()

            for i in range(4):
                nx = a+dx[i]
                ny = b+dy[i]

                if 0 <= nx <n and 0 <= ny < m:
                    if maps[nx][ny] == 1:
                        q.append((nx, ny))
                        maps[nx][ny] = maps[a][b] + 1

        ans = maps[n-1][m-1]

        return ans if ans > 1 else -1 # 예외처리 주의

    return bfs(0, 0)