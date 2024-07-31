n, m = map(int,(input().split()))
map = [list(map(int, input().split())) for _ in range(n)]
sum = 0
for i in range(n):
    cnt = 0
    for j in range(1,n):
        
        if map[i][j]==map[i][j-1]:
            cnt+=1
            if cnt == m-1:
                sum+=1
                break
        else:
            cnt=0

for j in range(n):
    cnt = 0
    #flag = False
    for i in range(1,n):
        
        if map[i][j]==map[i-1][j]:
            cnt+=1
            if cnt == m-1:
                sum+=1
                break
        else:
            cnt=0

print(sum)