s = "foo"
t = "bar"
pat ={}
st = {}
if len(s) == len(t) :
    i = 0
    while i < len(s):
        if s[i] in pat and pat[s[i]] != t[i]:
            print('false')
        if t[i] in st and st[t[i]]  != s[i]:
            print('false') 
        pat[s[i]] = t[i]
        st[t[i]] = s[i]
        i+=1
    print(pat)
    print(st)
else:
    print('False')
print('True')