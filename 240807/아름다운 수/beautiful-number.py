# 1을 1회 고른다.
# 2를 2회 고른다.
# 3을 3회 고른다.
# 4를 4회 고른다.

# 1~4을 더해서 n을 만드는 경우의 수 구하기

from sys import stdin, stdout
n = int(stdin.readline())
ans = 0

def dfs(cnt, a):
    global ans
    if a==0:
        ans+=1
        return

    for i in range(1,5):
        if a>=i:
            dfs(cnt+1, a-i)

dfs(0,n)
stdout.write(str(ans))