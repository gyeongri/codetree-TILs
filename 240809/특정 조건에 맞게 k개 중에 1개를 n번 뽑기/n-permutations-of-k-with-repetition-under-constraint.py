from sys import stdin, stdout
K, N = map(int, stdin.readline().split())

arr = [0 for _ in range(N)]

def dfs(cnt, arr):

    if cnt == N:

        stdout.write(" ".join(str(s) for s in arr)+"\n")
        return

    for i in range(1,K+1): #2개 이상 뽑았을 때부터..
        if cnt>1 and arr[cnt-1]==i and arr[cnt-1]==arr[cnt-2]: continue
        arr[cnt]=i
        dfs(cnt+1, arr)


dfs(0, arr)