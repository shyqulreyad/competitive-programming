# #fib(n) with out DP
def fib2(n):
    if n<=2:
        return 1
    return fib2(n-1) + fib2(n-2)
print(fib2(6))
# # print(fib2(50))




# #fib(n) with dynamic Programing Memoization
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

print(fib(6))
print(fib(50))