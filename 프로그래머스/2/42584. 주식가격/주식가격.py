def solution(prices):

    ans = []
    cnt = 0

    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[i] > prices[j]:
                break

        ans.append(cnt)
        cnt = 0

    return ans