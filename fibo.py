n=int(input("Enter the number of terms:"))
a=0
b=1
c=a+b
i=1
print("Fibonacci series :",end='')
while(i<=n):
   print(a,end=" ")
   i+=1
   a=b
   b=c
   c=a+b