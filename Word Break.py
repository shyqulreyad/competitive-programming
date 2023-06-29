Test ="testing"
test2 ="tedtinge"
s = "leetcode" 
wordDict = ["leet","code"]
s = "applepenapple"
wordDict = ["apple","pen"]
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
s = "aaaaaaa"
wordDict = ["aaaa","aaa"]
s.split()
word =''
matched = 0
target = len(s)
print(target)
j = 0
for i in s:
    # print(i)
    j+=1
    word+=i
    # print(word)
    if word in wordDict:
        print(word,'yes',j)
        matched +=j
        j=0
        word =''
    else:
        print(word,'no')

print(matched)
if target == matched:
    print('true')
else:
    print('false')
