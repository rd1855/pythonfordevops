num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

opr = input("Enter operator (+, -, *, /): ")

if opr == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif opr == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")   

elif opr == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif opr == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

elif opr == '%':
    result = num1 % num2
    print(f"{num1} % {num2} = {result}")        

elif opr == '**':
    result = num1 ** num2
    print(f"{num1} ** {num2} = {result}")           

else:
    print("Invalid operator. Please use one of +, -, *, /, %, **.")
    result = None
         