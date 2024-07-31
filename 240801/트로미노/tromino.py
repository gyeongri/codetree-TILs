from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

b1 = ((1,0), (1,1))
b2 = ((0,1), (0,2))
M = 0
for i in range(n-1):#b1
    for j in range(m-1):
        sum1 = arr[i][j]+arr[i+1][j]+arr[i+1][j+1]
        sum2 = arr[i][j]+arr[i][j+1]+arr[i+1][j+1]
        sum3 = arr[i][j+1]+arr[i+1][j]+arr[i+1][j+1]
        sum4 = arr[i][j]+arr[i][j+1]+arr[i+1][j]
        tmp = [sum1, sum2, sum3, sum4]
        tmpM = max(tmp)
        if tmpM > M : M = tmpM


for i in range(n):#b2-1
    for j in range(m-2):
        sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]
        if sum > M: M = sum

for i in range(n-2):#b2-2
    for j in range(m):
        sum = arr[i][j]+arr[i+1][j]+arr[i+2][j]
        if sum > M: M = sum

print(M)