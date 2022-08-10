# 1063 - 킹
# 체스판

import sys
    
# 변환
def change(str):
    ch = {'A': 1,'B': 2,'C': 3,'D': 4,'E': 5,'F': 6,'G': 7,'H': 8,
          1:'A', 2:'B', 3:'C', 4:'D', 5:'E', 6:'F', 7:'G', 8:'H'}.get(str)
    return ch

# 이동
def move(str):
    mv = {'R':(1, 0), 'L':(-1, 0), 'B':(0, -1), 'T':(0, 1), 
         'RT':(1, 1), 'LT':(-1, 1), 'RB':(1, -1), 'LB':(-1, -1)}.get(str)
    return mv

# 범위확인
def size(x, y, mx, my):
    x = x + mx
    y = y + my
    if 1 > x or x > 8 or  1 > y or y > 8:
        return False
    return True
    
king, stone, moveN = sys.stdin.readline().split()
n = int(moveN)

kingX = change(king[0])
kingY = int(king[1])
stoneX = change(stone[0])
stoneY = int(stone[1])

# 이동입력
for i in range(n):
    m = sys.stdin.readline().strip()
    mv = move(m)
    mX = mv[0]
    mY = mv[1]
    
    # 범위확인
    if not size(kingX, kingY, mX, mY):
        continue
    # 돌이 있는 위치로 이동하면서 돌의 범위가 벗어나지 않는지
    if stoneX == kingX + mX and stoneY == kingY + mY:
        if not size(stoneX, stoneY, mX, mY):
            continue
        stoneX = stoneX + mX
        stoneY = stoneY + mY
        
    kingX = kingX + mX
    kingY = kingY + mY
    
# 출력
print(change(kingX),kingY,sep='')
print(change(stoneX),stoneY,sep='')