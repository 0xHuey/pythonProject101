#Create a boolean varaiable

#is_male = True

#if is_male:
#    print("You are a male")


#Step 2 adding "else"

#is_male = True

#if is_male:
#    print("You are a male")
#else:
#    print("You are not a male")

#Step 3 running "if" and "or" statements

#is_male = True
#is_tall = True

#if is_male or is_tall:
#    print("You are a male or tall or both")
#else:
#    print("You are neither male nor tall")

#Step 4 Using "and"

#is_male = False
#is_tall = False

#if is_male and is_tall:
#    print("You are a male or tall or both")
#else:
#    print("You are neither male nor tall")

#Step 4 "elif:

#is_male = Tall
#is_tall = False

#if is_male and is_tall:
#    print("You are a male or tall or both")
#elif is_male and not(is_tall):
#    print("You are a short male")
#elif not(is_male) and is_tall:
#    print("You are a short male")
#else:
#    print("You are either male nor tall")

#Step 5 w/ "Comparisons"

#Types of operators "<" ">" "=!" "<=" ">="
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))