
num1 = float(input("Enter first number: "))
#Adding "float" means that the user has to input a number or there will be an error
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)

else:
    print("Invalid operator")
