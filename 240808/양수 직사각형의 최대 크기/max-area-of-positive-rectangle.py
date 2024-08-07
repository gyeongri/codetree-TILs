from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]

def check(a,b,c,d):
    # if a>=n or b>=n or c>=m or d>=m:
    #     return False
    for i in range(a,b):
        for j in range(c,d):
            if arr[i][j]<=0:
                return False
    return True

ans = -1
for i in range(1,n+1): # 가로 크기
    for j in range(1,m+1): # 세로 크기
        for p in range(n-i+1): # 어디서부터 어디까지 탐색할지(세로) - n=3, i=2 인 경우 0,1 탐색
            for q in range(m-j+1): # 어디서부터 어디까지 탐색할지(가로) - m=3, j=2인 경우 0,1, 탐색
                if check(p, p+i, q, q+j)==True: # p=0, q=1, i=2,j=2인 경우 -> check(0,2,1,3) -> 가로로 1,2, 세로로 0,1 탐색
                    if i*j > ans: ans = i*j

stdout.write(str(ans))