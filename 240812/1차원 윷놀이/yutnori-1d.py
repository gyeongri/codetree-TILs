from sys import stdin, stdout
# 1~m의 번호
# n번 이동한다.(뽑느다.)
n,m,k = map(int, stdin.readline().split())
#pan = [i for i in range(1,m+1)]

d = list(map(int, stdin.readline().split()))

arr = [0 for _ in range(n)]


def move(arr, d):
    x = [1 for _ in range(k+1)] # 각 말이 몇번째 칸에 있는지
    score = 0
    for i in range(n): # arr, d는 n번 뽑아서 이동하므로 n 사이즈
        if x[arr[i]] >= m:
            continue # 이미 m 이상인 경우에는 더하지 않고 그냥 패스함.   
        x[arr[i]] += d[i]
        if x[arr[i]] >=m :
            score += 1
    return score

# m번에 도달하면 1점을 얻는다.
# 말을 고르는 경우의 수 -> 중복 상관없이 m개중 1개를 선택하는 것을 n회 반복
max_score = 0
def dfs(cnt, arr):
    global max_score
    if cnt == n:
        new_score = move(arr,d)
        if new_score > max_score:
            max_score = new_score
        return
    for i in range(1,k+1):
        arr[cnt] = i
        dfs(cnt+1, arr)

dfs(0,arr)

print(max_score)