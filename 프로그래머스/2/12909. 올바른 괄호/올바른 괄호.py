def solution(s):

    stk = []

    for i in range(len(s)):
        if not stk: 
            if s[i] == '(':
                stk.append(s[i])

            else: return False

        else:
            if s[i] == ')':
                stk.pop()

            else:
                stk.append(s[i])


    if not stk:
        return True

    return False