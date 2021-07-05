# 프로그래머스 가장큰수

def solution(numbers):
    strNumber = [str(i) for i in numbers]
    strNumber.sort(key=lambda x: (x*4)[:4], reverse=True)
    if strNumber[0] == '0':
        return '0'
    return "".join(strNumber)


#
