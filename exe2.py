num=int(input("enter a number:"))
check=int(input("enter a number to be divided by:"))
if num%2>0:
        print(num,"is odd")
else:
        print(num,"is even")
if num%4==0:
    print(num,"is multiple of 4")
else:
    print(num,"isn't a multiple of 4")
if num%check==0:
    print(check,"divides",num,"evenly")
else:
    print(check,"doesn't divide",num,"evenly")
