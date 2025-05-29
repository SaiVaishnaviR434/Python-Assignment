#1.Write a function for arithmetic operators(+,-,*,/)
def arithmetic_opr(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: Cannot divide by zero")
arithmetic_opr(10, 5)

#2.Write a method for increment and decrement operators(++, --)
def increment_decrement(value):
    print("Original value:", value)
    value += 1
    print("After increment:", value)
    value -= 2
    print("After decrement:", value)
increment_decrement(3)

#3.Write a program to find the two numbers equal or not.
def check_equality(a, b):
    if a == b:
        print(f"{a} and {b} are equal.")
    else:
        print(f"{a} and {b} are not equal.")
check_equality(12,13)
check_equality(4,4)

#4.Program for relational operators (<,<==, >, >==)
def relational_opr(a, b):
    print(f"{a} < {b}:", a < b)
    print(f"{a} <= {b}:", a <= b)
    print(f"{a} > {b}:", a > b)
    print(f"{a} >= {b}:", a >= b)
relational_opr(5,4)
relational_opr(3,3)

#Print the smaller and larger number
def smaller_larger(a, b):
    smaller = min(a, b)
    larger = max(a, b)
    print("Smaller number:", smaller)
    print("Larger number:", larger)
smaller_larger(3,4)