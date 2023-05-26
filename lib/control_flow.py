#!/usr/bin/env python3

def admin_login(username, password):
    if username == 'admin' or username == 'ADMIN':
        return 'Access granted' if password == '12345' else 'Access denied'
    else:
        return 'Access denied'
    # your code here
    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature < 85:
        return "It's perfect out there!"
    else:
        return "It's too dang hot out there!"
    pass

def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num
    pass

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print('Invalid operation!')
        return None
    pass
