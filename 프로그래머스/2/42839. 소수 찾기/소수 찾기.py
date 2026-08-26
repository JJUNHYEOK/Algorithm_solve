from itertools import permutations
import math

def solution(numbers):
    
    def sosu(a):
        if a <= 1:
            return False
        
        for i in range(2, math.isqrt(a) + 1):
            if a % i == 0:
                return False
            
        return True
    
    
    number = set()
    
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num = int("".join(p))
            number.add(num)
            
    ans = 0
    
    for num in number:
        if sosu(num):
            ans += 1
            
    return ans
    