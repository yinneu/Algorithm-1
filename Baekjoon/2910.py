# 2910 - 빈도 정렬
import sys

count = {}
n , c = map(int, sys.stdin.readline().split())      # n -길이, c -최대 숫자
numlt = list(map(int, sys.stdin.readline().split()))

for num in numlt:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1
    
#value 기준으로 내림차순 정렬
sorted_count = sorted(count.items(), key = lambda item: item[1], reverse = True)

for i in sorted_count:
    for j in range(i[1]):
        print(i[0], end=' ')