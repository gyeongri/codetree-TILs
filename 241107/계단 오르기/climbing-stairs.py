from sys import stdin, stdout
N = int(stdin.readline())

dp = [0 for _ in range(1000)]
#print(dp)
dp[1] = 0
dp[2] = 1
dp[3] = 1

 # 2계단 아래에서 올라오는 경우 + 3계단 아래에서 올라오는 경우
for i in range(4,N+1):
    dp[i] = dp[i-2]+dp[i-3]

print(dp[N] % 10007)