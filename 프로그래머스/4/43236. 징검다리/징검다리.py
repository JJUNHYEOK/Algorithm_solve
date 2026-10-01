def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    ans = 0 

    while left <= right:
        mid = (left+right)//2
        prev = 0
        remove = 0

        for rock in rocks:
            if rock - prev < mid:
                remove += 1

            else:
                prev = rock

        if distance - prev < mid:
            remove += 1

        if remove <= n:
            ans = mid
            left = mid + 1

        else:
            right = mid - 1

    return ans