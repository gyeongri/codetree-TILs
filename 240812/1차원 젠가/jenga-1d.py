from sys import stdin, stdout
n = int(stdin.readline()) #6
arr = [list(map(int,stdin.readline().split())) for _ in range(n)] # 젠가 배열
delete = [list(map(int, stdin.readline().split())) for _ in range(2)]   # 삭제할 인덱스 2개

for d in delete:
    tmp = []
    #arr[d[0]-1:d[1]-1][0] = 0

    for i in range(d[0]-1, d[1]): # 터진 칸 0으로 만들기 -> 1,2,3 인덱스(2~4)
        arr[i][0] = 0

    for i in arr:                 # 남은 칸 tmp 배열에 저장
        for j in i:
            if j != 0: tmp.append(j)

    for i in range(n):
        arr[i][0] = 0             # 젠가 배열 전부 0으로 만들기

    for i in range(len(tmp)):
        arr[i][0] = tmp[i]

s = 0
for i in arr:
    if i[0] > 0: s+=1

stdout.write(str(s)+"\n")
for i in arr:
    if i[0] > 0:
        stdout.write(str(i[0])+"\n")