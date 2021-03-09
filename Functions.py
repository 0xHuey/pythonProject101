#Basically a bunch of code that performs a thing
#Helps you to break up your code into different sections

#when writing "def" means you are writing a function
#can be written "sayhi" or "say_hi" doesnt really matter
#The function will be everything within the indented section

#def say_hi():
#    print("Hello Users")

#Call the function w/o calling the "Function" you wont print anything

#say_hi()

#Step 2 "Parameters"

def say_hi(name, age):
#takes 2 parameters
    print("Hello " + name + ", you are " + str(age))

say_hi("Mike", 39)
say_hi("Steve", 20)
