# 1012 - 유기농 배추
# DFS

import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):   
    #방문체크
    visited[x][y] = True
    
    #상하좌우 인접한 배추확인
    test = [(x-1,y),(x,y-1),(x+1,y),(x,y+1)]
    for t in test :
        tx = t[0]
        ty = t[1]
        
        # 배열을 벗어날 경우
        if tx < 0 or tx >= width or ty < 0 or ty >= height :
            continue
        
        # 아직 방문하지 않은 경우 방문
        if arr[tx][ty] == 1 and visited[tx][ty] == False:
            dfs(tx, ty)
           
  
testCase = int(input())
for test in range(testCase):
             
    #크기와 개수
    result = 0
    width,height,k = map(int,input().split())
    arr = [[0 for j in range(height)] for i in range(width)]

    #배추 위치 입력
    inputlt = []
    for i in range(k) :
        x,y = map(int,input().split())
        arr[x][y] = 1
        inputlt.append((x,y))

    # 방문여부  
    visited = [[0 for j in range(height)] for i in range(width)]

    # 검사
    for i in inputlt:
        if visited[i[0]][i[1]] == True :
            continue
        dfs(i[0], i[1])
        result += 1
        
    print(result)
  