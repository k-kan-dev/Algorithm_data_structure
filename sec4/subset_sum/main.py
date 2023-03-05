num, w = map(int, input().split())
a = list(map(int, input().split()))
ans = []


def subset_sum(n, target):
    if a[n] == target:
        ans.append(a[n])
        return True

    if n == 0:
        return False
    
    if subset_sum(n-1, target=target):
        return True
            
    if subset_sum(n-1, target-a[n]):
        ans.append(a[n])
        return True
    
    return False

subset_sum(num-1, w)
print(ans)
