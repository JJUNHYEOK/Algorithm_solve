from itertools import permutations

def solution(k, dungeons):
    ans = 0

    for p in permutations(dungeons):
        cur = k
        cnt = 0

        for min, use in p:
            if cur >= min:
                cur -= use
                cnt += 1

        ans = max(ans, cnt)

    return ans