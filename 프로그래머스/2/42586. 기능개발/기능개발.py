def solution(progresses, speeds):

    remain = []
    n = len(progresses)

    for i in range(n):
        if (100-progresses[i])%speeds[i] == 0:
            remain.append((100-progresses[i])//speeds[i])

        else:
            remain.append((100-progresses[i])//speeds[i] + 1)

    # remain = [7, 3, 9]

    cur = remain[0]
    cnt = 1
    ans = []

    for i in range(1, n):
        if remain[i] <= cur:
            cnt += 1

        else:
            ans.append(cnt)
            cur = remain[i]
            cnt = 1

    ans.append(cnt)

    return ans