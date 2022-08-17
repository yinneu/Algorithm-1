# 2178 - 미로 탐색
# DFS : 시간초과
# BFS : 최단거리
from collections import deque
import sys
read = sys.stdin.readline

maze = []
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

#BFS
def move(x,y):
    queue = deque([[x,y]])   
    shortest[x][y] = 1
    
    while queue:
        nx = queue[0][0]
        ny = queue[0][1]        
        queue.popleft()

        # 상하좌우
        for i in range(4):
            gx = nx + dx[i]
            gy = ny + dy[i]
            
            # 범위확인      
            if 0 <= gx < n and 0 <= gy < m:
                # 경로와 방문확인       
                if maze[gx][gy] == 1 and shortest[gx][gy] == -1: 
                    shortest[gx][gy] = shortest[nx][ny] + 1          
                    queue.append([gx,gy])        
            

n, m = map(int,read().split())

# 최단거리
shortest = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    row = list(map(int,str(read().strip())))
    maze.append(row)
        
move(0, 0)
print(shortest[n-1][m-1])   