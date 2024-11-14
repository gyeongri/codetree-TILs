from sys import stdin, stdout
months = [0,31,28,31,30,31,30,31,31,30,31,30,31]

m1, d1, m2, d2 = map(int, stdin.readline().split())

if m1 == m2:
    ans = d2 - d1 + 1
else:
    ans = months[m1] - d1 + 1 + d2
    for i in range(m1+1, m2):
        ans+=months[i]

stdout.write(str(ans))
