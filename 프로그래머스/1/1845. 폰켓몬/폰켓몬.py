def solution(nums):
    
    N = len(nums)
    goyu = len(set(nums))
    
    ans = min(N//2, goyu)
    
    return ans
    
    
    
    