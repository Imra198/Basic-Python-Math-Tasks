# WORKSHEET P2 EXERCISES

import math

def areaOfCircle():
    radius = float(input("Enter the radius of a circle: "))
    area = math.pi * radius ** 2
    print("Area of the circle is", area)

def circumferenceOfCircle():
    radius = float(input("Enter the radius of a circle: "))
    circumference = 2 * math.pi * radius
    print("Circumference of the circle is", circumference)

def costOfPizza():
    diameter = float(input("Enter the diameter of the pizza: "))
    radius = diameter / 2
    area = math.pi * radius ** 2
    price = 1.5 * area
    print("Price for the pizza:", price)

def slopeOfLine():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    slope = (y2 - y1) / (x2 - x1)
    print("Slope of the line:", slope)

def distanceBetweenPoints():
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("Distance between the points:", distance)

def travelStatistics():
    speed = float(input("Enter the average speed: "))
    time = float(input("Enter the duration: "))
    distance = speed * time
    amount = distance / 5
    print("Distance traveled:", distance)
    print("Amount:", amount)

def sumOfSquares():
    n = int(input("Enter a number: "))
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    print("Sum of squares multiplied by 14:", 14 * total)

def averageOfNumbers():
    count = int(input("How many numbers? "))
    total = 0
    for i in range(count):
        num = int(input(f"Enter number {i+1}: "))
        total += num
    average = total / count
    print("Average:", average)

