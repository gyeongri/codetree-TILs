from sys import stdin, stdout

def print_dfs2(depth):
    global N
    if depth == 0:
        return

    stdout.write(str(depth)+" ")
    print_dfs2(depth-1)


def print_dfs(depth):
    global N
    if depth == 0:
        return

    stdout.write(str(N-depth+1)+" ")
    print_dfs(depth-1)

N = int(stdin.readline())
print_dfs(N)
stdout.write("\n")
print_dfs2(N)