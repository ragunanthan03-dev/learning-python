# This is a simple calculator program that can perform basic arithmetic operations.
num_1=float(input("Enter the first number: ")) #Gets input from the user and converts it to a float
num_2=float(input("Enter the second number: "))
operation=input("Enter the operation you want to perform (+, -, *, /): ") #Gets input from the user for the operation they want to perform
if operation == "+":
    result=num_1+num_2
    print("The result is: ", result)
elif operation == "-":
    result=num_1-num_2
    print("The result is: ", result)
elif operation == "*":
    result=num_1*num_2
    print("The result is: ", result)
elif operation == "/":
    if num_2 != 0: #Checks if the second number is not zero to avoid division by zero error
        result=num_1/num_2
        print("The result is: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of the following: +, -, *, /.") #Handles invalid operation input from the user