def solution(word):
    ex = ['A', 'E', 'I', 'O', 'U']
    dic = []

    def dfs(cur):
        if cur:
            dic.append(cur)

        if len(cur) == 5:
            return

        for e in ex:
            dfs(cur + e)

    dfs("")

    return dic.index(word) + 1