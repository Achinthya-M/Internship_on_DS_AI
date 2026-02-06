"""
def greet():
    print("Hello, welcome to internship!")
greet()
"""
"""
def add_numbers(a,b):
    return a+b
result = add_numbers(5,3)
print(result)
"""
"""
x=10
def show_value():
    x=5
    print(x)
show_value()
print(x)
"""
"""
food ="Pizza"
def junkfood():
    food="Burger"
    juice="Pista"
    print(food,"is not good for health")
junkfood()
print(food,"contains maida")
"""
"""
import math
import random
print(math.sqrt(16))
print(random.randint(1,50))
"""

#task 1
def calc_rectangle(length, width):
    area = length*width
    perimeter=2*(length+width)
    return area,perimeter
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area, perimeter = calc_rectangle(length, width)
print(f"Area: {area}, Perimeter: {perimeter}")