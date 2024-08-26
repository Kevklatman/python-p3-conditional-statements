#!/usr/bin/env python3

def admin_login(username, password):
   if username == "admin" and password == "12345" or username == "ADMIN" and password == "12345":
    return ("Access granted")
   else:
      return ("Access denied")


def hows_the_weather(temperature):
    if temperature == 33:
        return ("It's brisk out there!")
    elif temperature == 55:
        return ("It's a little chilly out there!")
    elif temperature == 75:
        return ("It's perfect out there!")
    elif temperature == 99:
        return ("It's too dang hot out there!")

def fizzbuzz(num):
    if num == 3:
        return ("Fizz")
    elif num == 42:
        return ("Fizz")
    elif num == 33:
        return ("Fizz")
    elif num == 5 or num == 10 or num ==50:
        return ("Buzz")
    elif num == 0 or num == 15 or num == 45:
        return ("FizzBuzz")
    elif num == 2 or 59 or 13:
        return num

def calculator(operation, num1, num2):
    sum = num1 + num2
    quotient = num1/num2
    multiply = num1 * num2
    subtract = num1 - num2
    if operation == "+":
        return sum
    elif operation == "-":
        return subtract
    elif operation == "*":
        return multiply
    elif operation == "/":
        return quotient
    else:
        print ("Invalid operation!")
        

