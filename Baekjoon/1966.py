# 1966 - 프린터큐
from collections import deque
import sys
read = sys.stdin.readline

#테스트 케이스수
testCase = int(read())

for t in range(testCase):  
    
    # 문서 개수와 궁금한 문서의 위치
    n, m = map(int,read().split())
    priority = list(map(int,read().split()))
    
    # 중요도와 처음 큐에서의 위치
    queue = deque([])    
    for i in range(n):
        queue.append([priority[i], i])
        
    target = queue[m]
    printCount = 0
    
    while queue:
        flag = False
        x = queue[0]      
        for i in range(1,len(queue)):
            # 더 중요한 문서가 있을때  
            if x[0] < queue[i][0]:
                flag = True
                break
                  
        if flag:
            queue.popleft()
            queue.append(x)
        else:
            q = queue.popleft()
            printCount += 1
            if q == target:
                print(printCount)
                break