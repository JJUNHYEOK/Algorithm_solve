def solution(k, dungeons):
    
    n = len(dungeons)
    visited = [False]*n
    max_cnt = 0
    
    def dfs(cur_k, cnt):
        nonlocal max_cnt
        
        max_cnt = max(max_cnt, cnt)
        
        for i in range(n):
            min_req, consume = dungeons[i]
            
            if not visited[i] and cur_k >= min_req:
                visited[i] = True
                dfs(cur_k - consume, cnt+1)
                visited[i] = False
                
    dfs(k, 0)
    
    return max_cnt