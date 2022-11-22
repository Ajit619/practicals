# without recursion

a=int(input("Enter the first number of the series "))
b=int(input("Enter the second number of the series "))
n=int(input("Enter the number of terms needed "))
print(a,b,end=" ")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
    n=n-1
    
    
 the time complexity would be O(n) since we only loop through it once
 space complexity would be O(N) 
 
 

#with recursion

def FibRec(a):  

   if a <= 1:  

       return a  

   else:  

       return(FibRec(a-1) + FibRec(a-2))  

aterms = int(input("Enter the terms? ")) 

  
if aterms <= 0:  

   print("Please enter a positive integer")  

else:  

   print("Fibonacci sequence:")  

   for z in range(aterms):  

       print(FibRec(z),end=" ")
       
For recursion, the time complexity would be O(2^n) since every node will split into two subbranches.

And the space complexity would be O(N) since the depth of the tree will be proportional to the size of n.
