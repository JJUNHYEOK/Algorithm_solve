def solution(answers):
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]
    person = [0]*3
    n = len(answers)
    
    for i in range(n):
        ans = answers[i]
        if ans == patterns[0][i%len(patterns[0])]:
            person[0] += 1
        if ans == patterns[1][i%len(patterns[1])]:
            person[1] += 1
        if ans == patterns[2][i%len(patterns[2])]:
            person[2] += 1

    max_score = max(person)
    result = []
    
    for i in range(len(person)):
        if person[i] == max_score:
            result.append(i+1)
            
    return result