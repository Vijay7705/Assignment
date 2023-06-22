n = int(input("Enter the number of terms:"))
l=[]
for i in range(n):
    no=int(input("Enter a number:"))
    l.append(no)
print("Input list:"l)
for x in l:
    if x>0:
        print(x,end=" ")
    else:
        continue
