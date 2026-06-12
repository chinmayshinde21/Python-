# Step 1: Take two numbers as input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step 2: Perform arithmetic operations (addition, subtraction, multiplication, and division)
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else None

# Step 3: Print the results cleanly
print(f"\nResults:")                                                 # f given in this program is used to format the string or f-string without using f-string we will get curly braces {} in output instead of values of num1 and num2
print(f"Addition ({num1} + {num2}) = {addition}")
print(f"Subtraction ({num1} - {num2}) = {subtraction}")
print(f"Multiplication ({num1} * {num2}) = {multiplication}")

# Step 4: Handle division carefully to avoid division by zero error
if num2 != 0:
    division = num1 / num2
    print(f"Division ({num1} / {num2}) = {division}")
if num1 != 0:
    division = num1 / num2
    print(f"Division ({num1} / {num2}) = {division}")
else:
    print("Division (Error) = Cannot divide by zero!")
