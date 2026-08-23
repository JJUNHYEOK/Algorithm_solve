def solution(arr):
    ans = []

    for num in arr:
        if not ans or ans[-1] != num:
            ans.append(num)

    return ans

print(solution([1,1,3,3,0,1,1]))
            
    
        
        