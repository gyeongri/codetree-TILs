from sys import stdin, stdout
n, t = map(int, stdin.readline().split())
tt = t % (n)
N = n*3

arr = list(map(int, stdin.readline().split()))
arr.extend(map(int, stdin.readline().split()))
arr.extend(map(int, stdin.readline().split()))

arr2 = arr[-tt:]+arr[0:N-tt]


for i in range(0, N, n):
    stdout.write(" ".join(map(str,arr2[i:i+n]))+"\n")