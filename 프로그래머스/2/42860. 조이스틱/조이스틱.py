def solution(name):
    cnt = 0
    n = len(name)
    
    # up-down
    for char in name:
        cnt += min(ord(char) - ord('A'), ord('Z') - ord(char)+1)
        
    # left-right
    min_move = n-1
    
    for i in range(n):
        next_i = i+1
        
        while next_i < n and name[next_i] == 'A':
            next_i += 1
            
        move_right_first = 2*i + (n-next_i)
        move_left_first = 2*(n-next_i) + i
        
        min_move = min(min_move, move_right_first, move_left_first)
        
    return cnt + min_move
    
    