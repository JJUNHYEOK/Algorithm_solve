from collections import Counter

def solution(participant, completion):
    
    cnt = Counter(participant) - Counter(completion)
    
    for name in cnt:
        return name