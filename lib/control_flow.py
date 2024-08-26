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
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
