from collections import deque

def solution(n, wires):
    graph = [[] for _ in range(n+1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def bfs(start, u, v):
        visited = [False]*(n+1)
        q = deque([start])
        visited[start] = True
        cnt = 1

        while q:
            cur = q.popleft()

            for nxt in graph[cur]:
                if (cur == u and nxt == v) or (cur == v and nxt == u):
                    continue

                if not visited[nxt]:
                    visited[nxt] = True
                    q.append(nxt)
                    cnt += 1

        return cnt
                
    min_diff = float("INF")

    for u,v in wires:
        cnt1 = bfs(u, u, v)
        cnt2 = n - cnt1

        diff = abs(cnt1 - cnt2)
        min_diff = min(min_diff, diff)

    return min_diff