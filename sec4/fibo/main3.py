n = int(input())

### initialize
memo = [-1] * (n+1)
memo[0] = 0
memo[1] = 1

def fibo(n):
    ### base case
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    ### cache
    if memo[n] != -1:
        return memo[n]
    
    ### recursive
    return fibo(n-1) + fibo(n-2)

print(f"fibo: {fibo(n)}")
