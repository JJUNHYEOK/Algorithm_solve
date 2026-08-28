def solution(prices):

    n = len(prices)
    ans = [0]*n
    stk = []

    for i in range(n):
        idx = i
        price = prices[i]

        while stk and prices[stk[-1]] > price:
            prev = stk.pop()
            ans[prev] = idx - prev

        stk.append(idx)

    while stk:
        prev = stk.pop()
        ans[prev] = (n-1) - prev

    return ans