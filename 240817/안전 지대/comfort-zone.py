from sys import stdin, stdout

N, M = map(int, stdin.readline().split())
town = [list(map(int, stdin.readline().split())) for _ in range(N)]

safe_area = 0
area_size = 0

dy = [0,-1,1,0,0]
dx = [0,0,0,-1,1]

# 마을이 모두 잠기는 순간 -> for문에서 범위 지정 시 써야하므로 미리 1을 더해 놓는다.
max_K = max(map(max, town)) + 1


def dfs(y, x, K, v):
    global N,M,town,area_size
    
    for i in range(5):
        ty = y+dy[i]
        tx = x+dx[i]
        if ty>=0 and ty<N and tx>=0 and tx<M and v[ty][tx]==False and town[ty][tx]>K:
            area_size += 1
            v[ty][tx] = True
            dfs(ty, tx,K, v)


# 최대 안전영역 개수
ans_K = 1
ans_cnt = 0

for K in range(1, max_K):
    v = [[False for _ in range(M)] for _ in range(N)]
    safe_area = 0

    for i in range(N) :
        for j in range(M):
            area_size = 0
            #각 자리에서 탐색을 시작했을 때, 1~N*M 사이즈의 안전영역이 발생했다면 안전영역 개수 증가!
            dfs(i,j,K, v)

            if area_size > 0:
                safe_area+=1


    if ans_cnt < safe_area:
        ans_cnt = safe_area
        ans_K = K
        

stdout.write(str(ans_K)+" ")
stdout.write(str(ans_cnt))