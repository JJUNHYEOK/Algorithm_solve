def solution(routes):

    # (-20, -15)
    # (-14, -5)
    # (-18, -13)
    # (-5, -3)

    n = len(routes)
    routes.sort(key=lambda x: x[1])
    cam = -int(1e9)
    cnt = 0

    for i in range(n):
        if cam < routes[i][0]:
            cam = routes[i][1]
            cnt += 1

    return cnt