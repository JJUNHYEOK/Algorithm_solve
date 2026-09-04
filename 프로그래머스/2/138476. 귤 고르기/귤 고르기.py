from collections import Counter

def solution(k, tangerine):
    
    cnts = Counter(tangerine)
    sorted_cnts = sorted(cnts.values(), reverse=True)
    
    ans = 0
    
    for cnt in sorted_cnts:
        ans += 1
        k -= cnt
        
        if k <= 0:
            break
            
    return ans
