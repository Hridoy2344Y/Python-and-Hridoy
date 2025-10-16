a=int(input("Enter your age:"))
if a>=18:
    print("You are eligible to vote")
elif a<18:
 print("You are not ready yet \n And you have more", 18-a, "years left")
else:
   print("You have given invalid character!!")