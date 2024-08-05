from sys import stdin, stdout
N,M = map(int, stdin.readline().split())
# 1~N의 숫자 중 M개 고르기

v = [False for _ in range(N+1)]
arr = [0 for _ in range(M)]

def dfs(cnt, idx):
    if cnt == M:# N개 다 골랐으면 return
        for i in range(M):
            stdout.write(str(arr[i])+" ")
        stdout.write("\n")
        return

    
    for i in range(idx,N+1):
        arr[cnt] = i
        dfs(cnt+1, i+1)


dfs(0, 1)