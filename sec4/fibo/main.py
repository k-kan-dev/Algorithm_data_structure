def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    
    return fibo(n-2) + fibo(n-1)

n = int(input())
print(f"fibo: {fibo(n)}")
