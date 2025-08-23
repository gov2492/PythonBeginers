####### simple operation using this calculator ########
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
operator = input("Enter operator: ")
if operator == '+' :
    print(firstNumber+secondNumber)
elif operator == '-':
    print(firstNumber-secondNumber)
elif operator == '*':
    print(firstNumber*secondNumber)
else:
    print(firstNumber/secondNumber);