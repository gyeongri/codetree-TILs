from sys import stdin
n,t = map(int, stdin.readline().split())

arr = list(map(int, stdin.readline().split()))
arr2 = list((map(int, stdin.readline().split())))
arr.extend(arr2)

t2 = t%(2*n)

new_arr = arr[-t2:]+arr[:n*2-t2]

for i in range(n):
    print(new_arr[i], end= " ")

print()

for i in range(n, 2*n):
    print(new_arr[i], end = " ")