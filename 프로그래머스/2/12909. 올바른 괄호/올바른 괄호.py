def solution(s):
    stk = []

    for char in s:
        if char == '(':
            stk.append(char)

        else:
            if not stk:
                return False
            stk.pop()

    if len(stk) == 0:
        return True

    return False