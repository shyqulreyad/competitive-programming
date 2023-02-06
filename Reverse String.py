s = ["h","e","l","l","o"," ","w","o","r","l","d"]
lenght = len(s)
# print(lenght)
for i in range(lenght//2):
    # print(i)
    # print(s[i],s[lenght-i-1])
    # print(s[lenght-i-1],s[i])
    s[i],s[lenght-i-1] = s[lenght-i-1],s[i]
print(s)

# Tuple unpacking
t = 1
k = 2
l = 3
a, b, c = t, k, l
print(a, b, c)