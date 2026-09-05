def solution(n, lost, reserve):

    nn = [1]*(n+1)
    cnt = 0

    for num in reserve:
        nn[num] = 2

    for num in lost:
        if num in reserve:
            nn[num] = 1

        else:
            nn[num] = 0

    for i in range(1, n+1):
        if nn[i] == 0:
            if i > 1 and nn[i-1] == 2:
                nn[i] = 1
                nn[i-1] = 1

            elif i < n and nn[i+1] == 2:
                nn[i] = 1
                nn[i+1] = 1

    for n in nn:
        if n >= 1:
            cnt += 1

    return cnt - 1