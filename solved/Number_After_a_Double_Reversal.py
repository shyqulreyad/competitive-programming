x = 0
if x < 0:
    x= abs(x)
sttr_1 = str(x)
reverse_1 = sttr_1[::-1]
reverse_num_1 = int(reverse_1)
sttr_2 = str(reverse_num_1)
reverse_2 = sttr_2[::-1]
reverse_num_2 = int(reverse_2)
if reverse_num_2 == x:
    print('true')
else:
    print('false')