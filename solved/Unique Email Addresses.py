emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
temp = []
for i in emails:
    print(i)
    local_name = i.split('@')[0]
    domain_name = i.split('@')[1]
    local_name = local_name.split('+')[0]
    local_name = local_name.replace('.','')
    i = local_name+'@'+domain_name
    if i not in temp:
        temp.append(i)
print(len(temp))
print(temp)