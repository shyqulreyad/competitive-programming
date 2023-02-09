def add_digits(n):
    res = 0
    for i in str(n):
        res+=int(i)
    if res > 9:
        return add_digits(res)
    else:
        return res

print(add_digits(1654))