from collections import deque

def solution(begin, target, words):
    n = len(words)
    visited = [False]*n

    def bfs(word):
        q = deque()
        q.append((begin,0))

        while q:
            cur, dist = q.popleft()

            for i in range(n):
                if visited[i]:
                    continue

                diff = 0

                for j in range(len(cur)):
                    if cur[j] != words[i][j]:
                        diff += 1

                if diff == 1:
                    q.append((words[i], dist+1))
                    visited[i] = True

                    if words[i] == target:
                        return dist + 1

        return 0

    return bfs(begin)