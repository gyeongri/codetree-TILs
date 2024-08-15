from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

v = [[False for _ in range(m)] for _ in range(n)]
dy = [1,0]
dx = [0,1]
ans = 0

def dfs(y, x):
    global n,m, arr, v, dy, dx, ans
    if y==n-1 and x==m-1:
        ans = 1
        return

    for i in range(2):
        ty = y+dy[i]
        tx = x+dx[i]
        if ty>=0 and ty<n and tx>=0 and tx<m and v[ty][tx]==False and arr[ty][tx]==1:
            v[ty][tx] = True
            dfs(ty,tx)
            v[ty][tx] = False

dfs(0,0)
stdout.write(str(ans))