def solution(progresses, speeds):

    days = []

    for i in range(len(progresses)):
        if (100 - progresses[i])%speeds[i] == 0:
            days.append((100 - progresses[i])//speeds[i])

        else:
            days.append((100 - progresses[i])//(speeds[i])+1)

    cur = days[0]
    cnt = 1
    ans = []

    for i in range(1, len(progresses)):
        if days[i] <= cur:
            cnt += 1

        else:
            ans.append(cnt)
            cur = days[i]
            cnt = 1

    ans.append(cnt)

    return ans