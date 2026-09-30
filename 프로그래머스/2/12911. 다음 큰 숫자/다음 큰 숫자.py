def solution(n):
    origin = n

    while True:
        n += 1
        target = n

        a = list(str(bin(origin)))
        b = list(str(bin(target)))

        if a.count('1') == b.count('1'):
            break

    return target