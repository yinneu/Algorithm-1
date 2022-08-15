# 1874 - 스택 수열
import sys

stack = []
result = []
check = True
count = 1 
n = int(sys.stdin.readline())

# 입력
for i in range(n):
    num = int(sys.stdin.readline())
    # pop될 수까지 push
    while count <= num:
        stack.append(count)
        result.append('+')
        count += 1
    
    #top과 비교하여 pop    
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        check == False
        break

if not check:
    print('NO')
else:
    for i in result:
        print(i)
