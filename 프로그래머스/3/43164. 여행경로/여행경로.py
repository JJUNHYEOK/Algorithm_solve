def solution(tickets):
    N = len(tickets)
    tickets.sort() # 알파벳 순서 우선 탐색

    visited = [False]*N
    ans = []

    def dfs(cur, path):
        if len(path) == N+1: # 모든 티켓 사용 시
            ans.extend(path)

            return True # 유효 경로 찾았으므로 즉시 종료

        for i in range(N):
            if not visited[i] and tickets[i][0] == cur: # i번째 티켓이 사용되지 않았고 출발지가 현재 공항일 경우
                nxt = tickets[i][1]

                visited[i] = True
                path.append(nxt)

                if dfs(nxt, path): # 다음 공항으로 재귀 호출
                    return True

                visited[i] = False # 막다른 길에 도달한 경우 되돌리기
                path.pop()

        return False

    dfs("ICN", ["ICN"])

    return ans