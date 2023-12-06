def gcd(m, n):
    r = m // n
    s = m % n

    if s == 0:
        return n

    return gcd(m=n, n=r)

a, b = map(int, input().split())
print(gcd(a, b))
