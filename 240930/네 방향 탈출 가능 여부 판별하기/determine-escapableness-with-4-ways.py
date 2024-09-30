from sys import stdin, stdout
from collections import deque
n,m = map(int, stdin.readline().split())

arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
v = [[False for _ in range(m)] for _ in range(n)]

dy = [-1,1,0,0]
dx = [0,0,-1,1]

q =  deque([(0, 0)])
v[0][0] = True
while q:
    ty, tx = q.popleft()


    for dir in range(4):
        ny = ty + dy[dir]
        nx = tx + dx[dir]

        if ny==n-1 and nx == m-1:
            stdout.write("1\n")
            exit(0)

        if ny>=0 and nx>=0 and ny<n and nx<m and arr[ny][nx]==1 and v[ny][nx]==False:
            v[ny][nx] = True
            q.append((ny,nx))


stdout.write("0\n")