#1. program to print a name
name=input("Enter your name\n")
print(name)

#2. Write a program for a Single line comment and multi-line comments
# this is a single-line comment
"""
Hello Iam Sai Vaishnavi
B.Tech CSE graduate
Vaagdevi College of Engineering
"""
print("hello, comments in Python!")

#3.Define variables for different Data Types int, Boolean, char, float, double and print on the console
n=10
valid=True
name="name"
pi=3.14
print(type(n), n)
print(type(valid), valid)
print(type(name),name)
print(type(pi),pi)

#4.Define the local and Global variables with the same name and print both variables and understand the scope of the variables

# Global variable
x = 7

def my_function():
    # Local variable
    x = 5
    print("Local x inside function:", x)

#calling function
my_function()

# Printing the global variable
print("Global x outside function:", x)
