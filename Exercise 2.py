# Question 1: Arithmetic and Assignment Operators

# TODO: Add 3 to x using the += operator
x = 5
print("x=", x)
x += 3
print("x + 3 =", x)
# TODO: Multiply y by 2 using the *= operator
y = 10
print("y=", y)
y *= 2
print("y * 2 =", y)
# TODO: Divide x by y and store the result in a variable called 'result'
result = x / y   
print("result = x / y")   
# TODO: Print the value of 'result'
print("result=", result)

#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators

# TODO: Create a condition that checks if a is greater than b
a = 15
b = 10
print("a>b")
print(a>b)
# TODO: Create a condition that checks if b is even (hint: us")e the modulus operator)

print("is b even?")
print(b % 2 == 0)
# TODO: Create a condition that checks if c is less than or equal to a
c = 5
print("c = 5")


print(c <= a) 
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

final_condition = (a > b) or (b % 2 == 0 and c <= a)
print("Value of final_condition:", final_condition)

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = 55
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
# TODO: Print the grade for the given score

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1=6
num2=3
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = "+"

# TODO: Use conditional statements to perform the chosen operation on num1 and num2
# TODO: Handle the case of division by zero
if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."


# TODO: Print the result of the operation
print("Result:", result)
