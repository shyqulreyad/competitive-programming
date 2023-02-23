def fibnum(n,memo={}):
    if n in memo:
        return memo[n]
    if n== 0:
        return 0
    if n<=2:
        return 1
    memo[n] = fibnum(n-1,memo) + fibnum(n-2,memo)
    return memo[n]
print(fibnum(5))