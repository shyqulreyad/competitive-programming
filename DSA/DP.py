#fib(n) with out DP
def fib2(n):
    if n<=2:
        return 1
    return fib2(n-1) + fib2(n-2)
print(fib2(6))
# print(fib2(50))




#fib(n) with dynamic Programing Memoization
def fib(n,memo={}):
    if n in memo:
        return memo[n]
    if n<=2:
        return 1
    memo[n] = fib(n-1,memo) + fib(n-2,memo)
    return memo[n]

print(fib(6))
print(fib(50))
 
#Grid traveler with out dp
def gridTraveler(m,n):
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    return gridTraveler(m-1,n) + gridTraveler(m,n-1)

print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
# print(gridTraveler(18,18))

#grid traveler with dp
def gridTravelerDP(m,n,memo={}):
    key = str(m)+','+str(n)
    if key in memo:
        return memo[key]
    if m==1 and n==1:
        return 1
    if m==0 or n==0:
        return 0
    memo[key] = gridTravelerDP(m-1,n) + gridTravelerDP(m,n-1)
    return memo[key]

print(gridTravelerDP(1,1))
print(gridTravelerDP(2,3))
print(gridTravelerDP(3,2))
print(gridTravelerDP(3,3))
print(gridTravelerDP(18,18))