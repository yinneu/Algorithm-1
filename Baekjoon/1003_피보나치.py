#1003 - 피보나치 함수
#각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 출력하는 문제

import sys
def fibonacci(n) :
    temp = [0,0]
    if n in dic :
        return dic[n]
    else :
        n1 = fibonacci(n-1)
        n2 = fibonacci(n-2)
        temp[0] = n1[0] + n2[0]
        temp[1] = n1[1] + n2[1]
        dic[n] = temp
        return dic[n]


#각 테스트 케이스 리스트에 저장
#딕셔너리에 케이스마다 0과 1이 출력되는 횟수 저장
dic = { 0: [1,0], 1: [0,1]}
testlt = []
testCount = int(sys.stdin.readline())
for i in range(testCount) :
    test = int(sys.stdin.readline())
    testlt.append(test)
    fibonacci(test)

# 출력
for t in testlt :
    print(dic[t][0], dic[t][1])
