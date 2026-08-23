def solution(progresses, speeds):

    days = []

    for i in range(len(progresses)):
        target = 100 - progresses[i]

        if target%speeds[i] == 0:
            days.append(target//speeds[i])

        else:
            days.append(target//speeds[i] + 1)

    max_day = days[0]
    cnt = 1
    ans = []

    for i in range(1, len(days)):
        if days[i] <= max_day:
            cnt += 1

        else:
            ans.append(cnt)
            max_day = days[i]
            cnt = 1

    ans.append(cnt)

    return ans