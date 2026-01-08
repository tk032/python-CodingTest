def solution(a, b):
    answer = 0
    result_1 = int(str(a) + str(b))
    result_2 = int(str(b) + str(a))
    
    if result_1 >= result_2:
        answer = result_1
        return answer
    elif result_2 > result_1:
        answer = result_2
        return answer
    
    return answer

