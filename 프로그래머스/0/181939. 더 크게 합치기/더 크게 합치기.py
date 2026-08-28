def solution(a, b):
    
    str_a, str_b = str(a), str(b)
    val1 = int((str_a+str_b))
    val2 = int((str_b+str_a))
    
    ans = max(val1, val2)

    return ans