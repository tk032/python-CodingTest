def solution(n_str):
    answer = ''
    answer_list = list(n_str)
    for index, i in enumerate(n_str):
        if i == '0':
            answer_list.remove('0')
        else:
            break
    for i in answer_list:
        answer += i
        
    return answer
