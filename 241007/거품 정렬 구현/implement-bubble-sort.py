from sys import stdin, stdout
n = int(stdin.readline())
arr = list(map(int,stdin.readline().split()))


while(True):
    flag = False
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
            flag = True
    if not flag: break

for i in arr:
    stdout.write(str(i)+" ")