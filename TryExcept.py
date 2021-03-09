#How to handle potential errors for your code

#number = int(input("Enter a number: "))
#print(number)
#Using this and putting in a letter will break it

#Step 2 Adding a "Try block"

try:
    number = int(input("Enter the number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by Zero")
except ValueError:
    print("Invalid input")