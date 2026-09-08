def solution(money):

    def linear(arr):

        n = len(arr)

        if n == 0:
            return 0

        dp = [0]*(n+1)
        dp[1] = arr[0]

        for i in range(2, n+1):
            dp[i] = max(dp[i-2]+arr[i-1], dp[i-1])

        return dp[n]

    if len(money) == 1:
        return money[0]

    include_first = linear(money[1:])
    include_last = linear(money[:-1])

    return max(include_first, include_last)