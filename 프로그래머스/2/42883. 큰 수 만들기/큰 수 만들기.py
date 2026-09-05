def solution(number, k):
    stk = []

    for num in number:
        while stk and k > 0 and stk[-1] < num:
            stk.pop()
            k -= 1

        stk.append(num)

    if k > 0 :
        for _ in range(k-1, -1, -1):
            stk.pop()

    return "".join(stk)
    
    