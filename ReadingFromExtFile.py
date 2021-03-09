#You can use "r" to read the files, "w" to write the files in that txt file, "a" append a file in the file

employee_file = open ("employees.txt", "r")

print(employee_file.read())
#add "file.readable" to check if its true then switch to "file.read" to run the script

#print(employee_file.readline())
#this will read each line

#print(employee_file.readlines()[1])
#This will only read X line
employee_file.close()