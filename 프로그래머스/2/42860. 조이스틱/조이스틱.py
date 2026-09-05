def solution(name):

    cost = 0
    n = len(name)

    for char in name: # up - down
        up = ord(char) - ord('A')
        down = 26 - up
        cost += min(up, down)

    move = n - 1

    for i in range(n):
        nxt_idx = i + 1

        while nxt_idx < n and name[nxt_idx] == 'A':
            nxt_idx += 1

        move = min(move, 2*i + (n - nxt_idx), i + 2*(n - nxt_idx))

    cost += move

    return cost
    
    