def solution(my_string):
    answer = []
    total = ''
    for i in my_string[::-1]:
        total = i + total
        answer.append(total)
    
    answer.sort(reverse = False)
        
    return answer