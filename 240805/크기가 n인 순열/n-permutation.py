from sys import stdin, stdout
N = int(stdin.readline())

v = [False for _ in range(N+1)]
arr = [0 for _ in range(N)]

def dfs(cnt, arr):
    if cnt == N:
        for i in range(N):
            stdout.write(str(arr[i])+" ")
        stdout.write("\n")
        return

    
    for i in range(1,N+1):
        if v[i] == True : continue
        arr[cnt] = i
        v[i] = True
        dfs(cnt+1, arr)
        v[i] = False


dfs(0, arr)