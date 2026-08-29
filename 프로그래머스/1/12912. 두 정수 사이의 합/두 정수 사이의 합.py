def solution(a, b):
    answer = 0
    start = min(a, b)
    finish = max(a, b)
    
    for num in range(start, finish+1):
        answer += num
        
        
    return answer