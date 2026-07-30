def solution(distance, rocks, n):
    ans = 0
    left = 1
    right = distance

    rocks.sort()

    while left <= right:
        mid = (left+right)//2

        cur = 0
        rm = 0

        for rock in rocks:
            if rock - cur < mid:
                rm += 1

            else:
                cur = rock

        if distance - cur < mid:
            rm += 1

        if rm <= n:
            ans = mid
            left = mid + 1

        else: 
            right = mid - 1

    return ans