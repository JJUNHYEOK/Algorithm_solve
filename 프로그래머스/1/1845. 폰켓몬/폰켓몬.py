def solution(nums):
    
    N = len(nums)
    var = len(set(nums))
    
    ans = min(N//2 , var)
    
    return ans