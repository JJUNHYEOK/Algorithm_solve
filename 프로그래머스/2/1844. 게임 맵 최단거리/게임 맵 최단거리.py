from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    def bfs(sx, sy):
        q = deque()
        q.append((sx, sy))
        visited[sx][sy] = 0
        
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        
        while q:
            cx, cy = q.popleft()
            
            if cx == n-1 and cy == m-1:
                return maps[n-1][m-1]
            
            for d in range(4):
                nx, ny = cx+dx[d], cy+dy[d]
                
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] == 1:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                        maps[nx][ny] = maps[cx][cy] + 1
        
        return -1
                        
    return bfs(0, 0)