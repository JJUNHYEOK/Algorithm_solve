def solution(word):
    a = ['A', 'E', 'I', 'O', 'U']
    cmp = []

    def dfs(cur):
        if cur:
            cmp.append(cur)

        if len(cur) == 5:
            return

        for w in a:
            dfs(cur+w)
            
    dfs("")

    return cmp.index(word) + 1