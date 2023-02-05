s = ["h","e","l","l","o"]
lenght = len(s)
for i in range(lenght//2):
    s[i],s[lenght-i-1] = s[lenght-i-1],s[i]
print(s)
