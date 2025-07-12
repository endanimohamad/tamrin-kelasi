#محاسبه ی تعداد پرانتز و درستی کد
left = 0
right = 0
space = 0
free = 0
x = input("enter a code in python \n ")
for z in x:
    if z == "(" :
        left = left + 1
    elif z == ")" :
        right = right + 1
    elif z == " " :
        continue
    else:
        free = free + 1
if left == right :
    print("the code is correct")
else:
    print(f'your code has {free + left + right} character {left} ( {right} ) and is not correct')