from collections import Counter

def solution(participant, completion):
    
    val = Counter(participant) - Counter(completion)
    
    return list(val.keys())[0]
    
    
    
    