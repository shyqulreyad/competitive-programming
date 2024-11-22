n = 14

def is_ugly(num):
    if num <= 0:
        return False
    for factor in [2, 3, 5]:
        print('factor')
        print(factor)
        print('inside for')
        print(num)
        while num % factor == 0:
            print('factor')
            print(factor)
            print('inside whille before division')
            print(num)
            num //= factor
            print('inside whille after division')
            print(num)
    return num == 1

if is_ugly(n):
    print('true')
else:
    print('false')
# print(res)
