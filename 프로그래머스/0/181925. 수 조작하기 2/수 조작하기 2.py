def solution(numLog):
    answer = ''
    for index, i in enumerate(numLog):
        if index == 0:
            total = i
        else:
            if numLog[index] - numLog[index-1] == 1:
                answer += 'w'
            elif numLog[index] - numLog[index-1] == 10:
                answer += 'd'
            elif numLog[index] - numLog[index-1] == -1:
                answer += 's'
            elif numLog[index] - numLog[index-1] == -10:
                answer += 'a'
                
    return answer