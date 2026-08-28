def solution(num_list):
    
    N = len(num_list)
    
    for i in range(N):
        if num_list[i] < 0:
            return i
        
    return -1
            