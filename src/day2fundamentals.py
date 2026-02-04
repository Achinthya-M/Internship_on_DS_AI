age = 15
height = 5.4
_name = "Alice"
is_student = True
print(type(age))
print(type(height))
print(type(_name))
print(type(is_student))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    print("Sum:", a + b)
elif operation == '-':
    print("Difference:", a - b)
elif operation == '*':
    print("Product:", a * b)
elif operation == '/':
    if b != 0:
        print("Division:", a / b)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")

# Greeting program
name = input("Enter your name: ")
print("Hello,"+ name + "!")

#fstring
age = input("Enter your age: ")
print(f"My age is, {age}!")

#task 1
name = input("Enter your name: ")
age = int(input("Enter your current age: "))
print(f"Hey {name}, you will be {age+4} years old in 2030!")

#task 2
total_bill = float(input("Enter total bill amount:"))
people = int(input("Enter number of people:"))
split_bill = total_bill / people
print("Each person should pay:", split_bill)
print(type(total_bill))
print(type(people))
print(type(split_bill))

#task 3
item_name=str(input("enter the item name:"))
item_price=int(input("enter the item price:"))
item_qut=int(input("enter the quantity:"))
price=item_price*item_qut
in_stock=True
print(f"Item:{item_name}, Price:{item_price}, Qty:{item_qut},Total Price:{price},Available:{in_stock}")