def solution(n, lost, reserve):
    ans = 0
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    
    for student in sorted(real_lost):
        if student - 1 in real_reserve:
            real_reserve.remove(student-1)
            
        elif student + 1 in real_reserve:
            real_reserve.remove(student+1)
            
        else:
            n -= 1
            
    return n