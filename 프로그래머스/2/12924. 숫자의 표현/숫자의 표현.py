def solution(n):
    
    cnt = 0
    
    for start in range(1, n+1):
        pfx = 0
        
        for i in range(start, n+1):
            pfx += i
            
            if pfx == n:
                cnt += 1
                break
                
            elif pfx > n:
                break
                
    return cnt
        
    