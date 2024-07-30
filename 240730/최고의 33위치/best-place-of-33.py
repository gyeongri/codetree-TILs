N = int(input())
map = [list(map(int, input().split())) for _ in range(N)]

max = 0

for i in range(N-2):
    for j in range(N-2):
        sum = map[i][j]+map[i][j+1]+map[i][j+2]+map[i+1][j]+map[i+1][j+1]+map[i+1][j+2]+map[i+2][j]+map[i+2][j+1]+map[i+2][j+2]

        if sum>max: max = sum

print(max)