no=int(input("ENTER YOUR NUMBER"))
a=0
b=1
c=0
print("STEPS COUNTS----->",end="")
print(a,"",b,end=" ")
for i in range(0,no-2):
    c=a+b
    a,b=b,c
    print(c,end=" ")
print()
print("FIBONCCI NUMBER is {}".format(c))