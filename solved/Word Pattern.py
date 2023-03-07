pattern = "abba"
s = "dog cat cat dog"
pattern = "aaaa"
s = "dog cat cat dog"
k =s.split(' ')
pat ={}
st = {}
if len(pattern) == len(k) :
    i = 0
    while i < len(pattern):
        if pattern[i] in pat and pat[pattern[i]] != k[i]:
            print('false')
        if k[i] in st and st[k[i]]  != pattern[i]:
            print('false') 
        pat[pattern[i]] = k[i]
        st[k[i]] = pattern[i]
        i+=1
    print(pat)
    print(st)
else:
    print('False')
print('True')