def solution(arr):
    answer = []
    
    for i in range(len(arr)):
        iter = arr[i]
        for j in range(iter):
            answer.append(iter)
    return answer