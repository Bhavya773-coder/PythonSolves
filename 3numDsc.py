a=int(input("Enter the a"))
b=int(input("Enter the b"))
c=int(input("Enter the c"))
if (a>b):
    if(b>c):
        print(a,b,c)
    else:
        print(a,c,b)
else :
    if(c>a):
        print(c,b,a)
    else:
        print(b,a,c)