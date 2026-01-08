def solution(myString):
    answer = []
    myString_x = myString.split('x')
    answer = [len(i) for i in myString_x]
    return answer