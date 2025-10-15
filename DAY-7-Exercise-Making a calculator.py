a=int(input("Enter the 1st No."))
b=int(input("Enter the 2nd No."))
c= (input("What calculation is to be done (+,-,*,/):")) #The input is a complete function, It shows the message inside to the user and takes thier input and stores in the variable, for ex here =c
if c=="+":
     print(a+b)
    
elif c=="-":
     print(a-b)
    
elif c=="*":
     print(a*b)
    
if c=="/":
    print(a/b)
   
else:
    print("Your statement is wrong or you have given invalid operation")
