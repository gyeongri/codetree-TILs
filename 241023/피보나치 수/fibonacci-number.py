from sys import stdin, stdout
N = int(stdin.readline())
dp = [0 for _ in range(N)]
dp[0] = 1
dp[1] = 1

for i in range(2,N):
    dp[i] = dp[i-1]+dp[i-2]

# def fibo(n):
#     if n == 1:
#         return 1
#     else:
#         return fibo(n-1)

stdout.write(str(dp[N-1]))