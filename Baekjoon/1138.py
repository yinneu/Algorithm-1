# 1138 - 한 줄로 서기
import sys

num = int(sys.stdin.readline()) 
left = list(map(int,input().split()))

result = []    
for i in range(num):
    result.append(i+1)
    
for i in range(num-1,-1,-1):
    k = i   
    if left[result[k]-1] == 0:
        continue    
    #뒤로 이동하는데 뒤에 값이 나보다 작을 때는 카운트가 줄지 않음
    while left[result[k]-1]:
        # 뒤에 값이 현재 값보다 더 크면
        if result[k+1] > result[k]:
            left[result[k]-1] -= 1
        
        result[k], result[k+1] = result[k+1], result[k]
        k = k + 1

print(*result)