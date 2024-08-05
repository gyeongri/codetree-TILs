from sys import stdin, stdout
K, N = map(int, stdin.readline().split())
# 1~K의 숫자 중 N개 고르기
arr = []
def dfs(cnt, arr):
    if cnt == N:# N개 다 골랐으면 return
        for i in range(N):
            stdout.write(str(arr[i])+" ")
        stdout.write("\n")
        return

    for i in range(1,K+1):
        arr.append(i)
        dfs(cnt+1, arr)
        arr.pop()

dfs(0, arr)