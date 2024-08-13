from sys import stdin, stdout
N, M = map(int, stdin.readline().split()) # N개의 정점, M개의 간선
arr = [[] for _ in range(N+1)] # 정점 개수만큼 리스트 만들기 (0번 칸은 쓰지 않으므로 N+1 만큼 만들어야 함.)

v = [False for _ in range(N+1)] # 정점 번호 별 방문 여부(0번칸은 쓰지 않으므로 N+1만큼 만듦)
ans = 0

for i in range(M):
    a, b = map(int, stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)
# print(*arr, sep="\n")


# num = 정점 번호
def dfs(num):
    global ans, arr, v

    # 리프노드에 도달하면 ans를 1 증가 (XXXXX) -> 리프노드 개수를 세는게 아니라 거쳐가는 정점을 모두 더하는 것
    # if len(arr[num]) == 0 :
    #     ans += 1

    # num에서 출발해서 연결된 정점 탐색 시작하기
    for i in arr[num]:
        if v[i] == False:
            v[i] = True
            ans += 1
            dfs(i)

# 1번 정점부터 자식노드 탐색
v[1] = True
dfs(1)

stdout.write(str(ans))