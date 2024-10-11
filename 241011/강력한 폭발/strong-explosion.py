from sys import stdin, stdout
from pprint import pprint

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
max_area = 0

bomb_cnt = 0
bombs = []

def range_check(i):
    return (i>=0 and i<n)

def calc(v):
    s = 0
    for i in v:
        for j in i:
            if j: s += 1
    return s    

def explosion(nums, v): # nums 배열을 기반으로 순서대로 폭탄 터뜨리기
    for num in range(len(nums)):
        y = bombs[num][0]
        x = bombs[num][1]
        v[y][x] = True

        if nums[num] == 1:
            if range_check(y-1) and range_check(y-2) and range_check(y+1) and range_check(y+2):
                v[y-1][x]=True
                v[y-2][x]=True
                v[y+1][x]=True
                v[y+2][x]=True

        elif nums[num] == 2:
            if range_check(y-1) and range_check(x-1) and range_check(y+1) and range_check(x+1):
                v[y-1][x]=True
                v[y][x-1]=True
                v[y+1][x]=True
                v[y][x+1]=True      

        elif nums[num] == 3:
            if range_check(y-1) and range_check(x-1) and range_check(y+1) and range_check(x+1):
                v[y-1][x-1]=True
                v[y-1][x+1]=True
                v[y+1][x-1]=True
                v[y+1][x+1]=True
    a = calc(v)
    
    return a


def dfs(level):
    global bomb_cnt, nums, pick, max_area
    if level == bomb_cnt:
        v = [[False for _ in range(n)] for _ in range(n)]
        max_area = max(max_area, explosion(nums,v))

        return
    
    for i in range(1,4):# 폭탄개수만큼 반복하며 1~3 사이의 숫자 뽑기
        nums[level] = i
    
        dfs(level+1)


  
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 : 
            bomb_cnt +=1
            bombs.append([i,j])
pick = [0 for _ in range(bomb_cnt)]
nums = [0 for _ in range(bomb_cnt)] # 뽑은 배열
dfs(0)
stdout.write(str(max_area))