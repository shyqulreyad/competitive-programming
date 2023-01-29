ops = ["5","-2","4","C","D","9","+","+"]
ops = ["1","C"]
res = []
for i in ops:
    if i.isdigit():
        res.append(int(i))
    elif i.startswith("-") and i[1:].isdigit():
        res.append(int(i))
    else:
        print(i,'char',res[len(res)-1])
        if i == "C":
            del res[len(res)-1]
        elif i == "D":
            temp = 2*res[len(res)-1]
            res.append(temp)
        elif i == "+":
            temp = res[len(res)-2] + res[len(res)-1]
            res.append(temp)
print(sum(res))


"""
"5" - Add 5 to the record, record is now [5].
"-2" - Add -2 to the record, record is now [5, -2].
"4" - Add 4 to the record, record is now [5, -2, 4].
"C" - Invalidate and remove the previous score, record is now [5, -2].
"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
"9" - Add 9 to the record, record is now [5, -2, -4, 9].
"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
"""