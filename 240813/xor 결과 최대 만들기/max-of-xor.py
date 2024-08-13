from sys import stdin, stdout
n, m = map(int, stdin.readline().split())
numList = list(map(int, stdin.readline().split()))

arr = [0 for _ in range(m)]
v = [False for _ in range(n)]
M = 0

def xor(arr):
    global numList
    ans = 0 # xor하여 본인이 나오려면 0부터 시작해야함.
    for i in arr:
        ans = ans^numList[i]
    return ans


# n개 중에서 m개 뽑기
def combi(cnt, idx):
    global arr, M
    if cnt == m:
        M = max(xor(arr), M)
        return

    for i in range(idx, n): # 0 ~ n-1 인덱스 중에 뽑기 
        if v[i]==False:
            arr[cnt] = i
            v[i] = True
            combi(cnt+1, i)
            v[i] = False
combi(0,0)
stdout.write(str(M))