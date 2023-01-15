#first check if the box is bulky
print(pow(10,4))
print(pow(10,9))
length = 2000
width = 5000
height = 800
mass = 50
volume = length * width * height
bulky = False
heavy = False
if length >= 10000 or width >= 10000 or height >= 10000 or volume >= 1000000000:
    bulky = True
#check if heavy
if mass >= 100 :
    heavy = True

if bulky and heavy:
    print('both')
else :
    if bulky :
        print('bulky')
    if heavy :
        print('heavy')
    print('neighter')
