s = "abc"
t = "ahbgdc"
# s ="aaaaaa"
# t ="bbaaaa"
# s ="ab"
# t ="baab"
# s ="axc"
# t ="ahbgdc"
j =0
if len(s)<1:
    print('True')
for i in t:
    if i == s[j]:
        if j+1 <len(s):
            j+=1
        else:
            print('True')
print('False')