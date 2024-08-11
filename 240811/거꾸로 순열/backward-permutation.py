from sys import stdin, stdout
n = int(stdin.readline())


arr = [0 for _ in range(n)]
v = [False for _ in range(n+1)]
# 조합
def dfs(cnt, arr):
    if cnt==n:
        stdout.write(" ".join(map(str,arr))+"\n")
        return

    for i in range(n,0,-1):
        if v[i] == False:
            arr[cnt] = i
            v[i] = True
            dfs(cnt+1, arr)
            v[i] = False

dfs(0,arr)