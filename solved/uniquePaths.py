def uniqueP(m,n,memo={}):
    key = str(m)+','+str(n)
    if key in memo:
        return memo[key]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[key] = uniqueP(m-1,n,memo) + uniqueP(m,n-1,memo)
    return memo[key]
print(uniqueP(2,3))