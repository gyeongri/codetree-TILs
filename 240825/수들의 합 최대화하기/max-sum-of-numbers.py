from sys import stdin, stdout
n = int(stdin.readline())
arr = [list(map(int,stdin.readline().split())) for _ in range(n)]
p = [0 for _ in range(n)]
v = [False for _ in range(n)]

M = 0
# 행마다 하나씩 고르기
def dfs(cnt):
    global p,arr,M,v
    if cnt == n:
        M = max(M, sum(p))
        return
    
    for i in range(n):
        if v[i] == False:
            p[cnt] = arr[cnt][i]
            v[i] = True
            dfs(cnt+1)
            v[i] = False
dfs(0)
stdout.write(str(M))