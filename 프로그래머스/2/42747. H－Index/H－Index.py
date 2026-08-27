def solution(citations):

    citations.sort(reverse=True)

    h = 0

    for i in range(len(citations)):
        pcnt = i + 1
        ccnt = citations[i]

        if ccnt >= pcnt:
            h = pcnt

        else:
            break

    return h