def solution(myString):
    answer = ' '.join(sorted(myString.split('x'), reverse = False)).split()
    return answer