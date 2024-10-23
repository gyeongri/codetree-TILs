from sys import stdin, stdout
N = int(stdin.readline())

arr = [1 for _ in range(N)]
for i in range(2,N):
    arr[i] = arr[i-1]+arr[i-2]

stdout.write(str(arr[N-1]))