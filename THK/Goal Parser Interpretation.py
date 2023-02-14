command = "G()()()()(al)"
res = ''
check_next = False
i = 0
while i < len(command):
    if check_next:
        if command[i] ==')':
            res +='o'
        elif command[i] == 'a':
            res+='al'
            i+=2
    if command[i] == 'G':
        res+='G'
    else:
        check_next = True
    i+=1

print(res)

