from sys import stdin, stdout

n = int(stdin.readline())

arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
v = [[False for _ in range(n)] for _ in range(n)]

# 자기 자신 위치부터 탐색하므로 5방향 탐색
dy = [0,-1,1,0,0]
dx = [0,0,0,-1,1]


person_cnt = 0
town_arr = []

def dfs(y, x):
    global arr, v, dy, dx, person_cnt

    for i in range(5):
        ty = y+dy[i]
        tx = x+dx[i]
        if ty>=0 and ty<n and tx>=0 and tx<n and arr[ty][tx] == 1 and v[ty][tx] == False:
            person_cnt+=1
            v[ty][tx] = True
            dfs(ty, tx)

for i in range(n):
    for j in range(n):
        # 사람이 있고, 방문하지 않았다면 그 위치부터 dfs 시작, 주민수를 0으로 초기화함.
        if arr[i][j] == 1 and v[i][j]==False:
            person_cnt = 0
            dfs(i,j)
            town_arr.append(person_cnt)

town_arr.sort()
stdout.write(str(len(town_arr))+"\n")
for i in town_arr:
    stdout.write(str(i)+"\n")
#stdout.write(lambda i: str(i) for i in town_arr)