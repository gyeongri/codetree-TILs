from sys import stdin, stdout
n, r, c = map(int, stdin.readline().split())
nums = [list(map(int, stdin.readline().split())) for _ in range(n)]
dy = [-1,1,0,0]
dx = [0,0,-1,1]
r-=1
c-=1
stdout.write(str(nums[r][c])+" ")
flag = True
while(flag): 
    for k in range(4):
        ny = r+dy[k]
        nx = c+dx[k]
        if ny>=0 and ny<n and nx>=0 and nx<n and nums[ny][nx]>nums[r][c]:
            r = ny
            c = nx
            stdout.write(str(nums[r][c])+" ")
            break
        if k==3:
            flag = False
            break