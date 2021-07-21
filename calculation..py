print("welcome to the calculator to basic calculation work:")
num1=int(input("Enter the  Number1:"))
num2=int(input("Enter the Number2:"))
opt=input("please provide the operator...(+,-,*,/,%,)")
if opt=="+":
    print(num2+num1)
elif opt =="-":
    print(num2 - num1)
elif opt == "*":
    print(num2 * num1)
elif opt == "/":
    print(num2 / num1)
elif opt == "%":
    print(num2 % num1)

else:
    print("Invalid Operator")





