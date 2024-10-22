from sys import stdin, stdout

N = int(stdin.readline())

def dfs(depth):
    global N
    if depth == N:
        return

    for i in range(depth+1):
        stdout.write("*")
    stdout.write("\n")
    dfs(depth+1)


dfs(0)