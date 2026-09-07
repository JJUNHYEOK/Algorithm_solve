def solution(N, number):

    dp = [set() for _ in range(9)]
    dp[1] = {int(str(N))}

    if number in dp[1]:
        return 1

    # 수 이어붙이기
    for i in range(2, 9):
        dp[i].add(int(str(N)*i))

        # 사칙연산
        for k in range(1, i):
            for a in dp[k]:
                for b in dp[i-k]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)

                    if b != 0:
                        dp[i].add(a//b)

        if number in dp[i]:
            return i

    return -1