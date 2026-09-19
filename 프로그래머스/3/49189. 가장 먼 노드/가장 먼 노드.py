from collections import deque

def solution(n, vertex):

    graph = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    dis = [0]*(n+1)

    for i in range(len(vertex)):
            graph[vertex[i][0]].append(vertex[i][1])
            graph[vertex[i][1]].append(vertex[i][0])

    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                dis[nxt] = dis[cur] + 1
                q.append(nxt)

    ans = dis.count(max(dis))

    return ans