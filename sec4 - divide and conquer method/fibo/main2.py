import sys


n = int(input())

ans = [0] * (n+1)
ans[1] = 1

for i in range(n+1)[2:]:
    ans[i] = ans[i-1] + ans[i-2]

print(f"fibo: {ans[n]}")
