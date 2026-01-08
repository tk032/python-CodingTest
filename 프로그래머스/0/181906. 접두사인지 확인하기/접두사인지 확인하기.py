def solution(my_string, is_prefix):
    answer = 0
    total = 0
    
    if len(my_string) >= len(is_prefix):
        for i in range(len(is_prefix)):
            if my_string[i] == is_prefix[i]:
                total += 1  
    else:
        answer = 0
        
    if total == len(is_prefix):
        answer = 1
    else:
        answer = 0
            
    return answer