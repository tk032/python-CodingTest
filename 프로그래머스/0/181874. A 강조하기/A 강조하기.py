def solution(myString):
    answer = ''
    for index, i in enumerate(myString):
        if i == 'a' or i == "A":
            i = i.upper()
        else:
            i = i.lower()
        answer += i
        
    return answer