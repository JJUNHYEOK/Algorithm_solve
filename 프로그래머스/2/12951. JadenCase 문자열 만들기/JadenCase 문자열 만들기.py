def solution(s):
    ans = []
    start = True
    
    for ch in s:
        if ch == ' ':
            ans.append(ch)
            start = True
            
        else:
            if start:
                ans.append(ch.upper())
                start = False
            else:
                ans.append(ch.lower())
                
    return ''.join(ans)
            