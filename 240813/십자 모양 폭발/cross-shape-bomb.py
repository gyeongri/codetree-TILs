from sys import stdin, stdout

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
r, c = map(int, stdin.readline().split())
r -= 1
c -= 1
SIZE = arr[r][c]
arr[r][c] = 0

garo = []
sero = []

for i in range(1, SIZE):
    if r-i>=0:
        arr[r-i][c] = 0    
    if r+i<n:
        arr[r+i][c] = 0
    if c-i>=0:
        arr[r][c-i] = 0
    if c+i<n:
        arr[r][c+i] = 0


for i in range(n): # 가로 인덱스
    tmp = []
    for j in range(n-1,-1,-1): # 세로 인덱스 (아래부터)
        if arr[j][i] > 0:
            tmp.append(arr[j][i])


    # 터진 폭탄이 있는 경우에만 덮어씌우기
    if len(tmp) < n : 
        tmp = tmp + [0 for _ in range(n - len(tmp))] # 내려와서 생긴 빈 공간에는 0 넣기

        for j in range(n): # 해당 줄 새로 만든 배열로 덮어씌우기
            arr[n-1-j][i] = tmp[j] # 아래부터 채워야 하므로 (n-1)-j

for i in arr:
    for j in i:
        stdout.write(str(j)+" ")
    stdout.write("\n")

#print(*arr, sep="\n")