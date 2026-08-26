def solution(phone_book):
    
    hashmap = set(phone_book)
    
    for i in range(len(phone_book)):
        L = len(phone_book[i])
        
        for pfx in range(1, L):
            prefix = phone_book[i][:pfx]
            
            if prefix in hashmap:
                return False
            
    return True