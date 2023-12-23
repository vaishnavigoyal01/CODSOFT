def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error! Division by zero is not allowed.'
    else:
        return x / y

def modulus(x, y):
    return x % y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

operation = input("Enter the number of the operation you want to perform: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '1':
    print("Result:", add(num1, num2))
elif operation == '2':
    print("Result:", subtract(num1, num2))
elif operation == '3':
    print("Result:", multiply(num1, num2))
elif operation == '4':
    print("Result:", divide(num1, num2))
elif operation == '5':
    if num1.is_integer() and num2.is_integer():
        print("Result:", modulus(int(num1), int(num2)))
    else:
        print("Error! Modulus operation can only be performed on integers.")
else:
    print("Invalid operation selection.")