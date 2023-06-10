file=input("Input the filename")
f=file.split(".")
#f[-1] returns the extension as ."ext"
if(f[-1]=='py'):
    print("The extension of the file is:'python'")
elif(f[-1]=='c'):
    print("The extension of the file is:'C'")
elif(f[-1]=='java'):
    print("The extension of the file :",f[-1])

