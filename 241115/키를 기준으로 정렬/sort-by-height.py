from sys import stdin, stdout
n = int(stdin.readline())
arr = [[] for _ in range(n)]
for i in range(n):
    arr[i] = list(map(str, stdin.readline().split()))

arr = sorted(arr, key = lambda x: x[1])
for i in range(n):
    for j in range(3):
        stdout.write(arr[i][j] +" ")
    stdout.write("\n")