def solution(answers):
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    scores = [0]*3

    for idx, answer in enumerate(answers):
        for person, pattern in enumerate(patterns):
            if answer == pattern[idx%len(pattern)]:
                scores[person] += 1

    max_score = max(scores)

    result = []

    for i, score in enumerate(scores):
        if score == max_score:
            result.append(i+1)

    return result