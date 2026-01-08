def solution(num_list):
    num_multi = 1
    num_sum = 0
    
    for i in num_list:
        num_multi = num_multi * i
        num_sum += i 
        
    num_sum = num_sum ** 2  
    
    if num_multi < num_sum:
        answer = 1
    else:
        answer = 0
    return answer

