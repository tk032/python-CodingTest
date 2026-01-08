def solution(strArr):
    answer = strArr
    print(len(answer))
    for i in range(1,len(answer),2):
        answer[i] = answer[i].upper()
    for i in range(0,len(answer),2):
        answer[i] = answer[i].lower()
    return answer