#1. Write a program to print “Bright IT Career” ten times using for loop
for i in range(10):
    print("Bright IT Career")

#2.Write a program to print 1 to 20 numbers using the while loop
i = 1
while i <= 20:
    print(i)
    i += 1

#3 Program to equal operator and not equal operators
a = 10
b = 20
print("a == b:", a == b)
print("a != b:", a != b)

#4. Write a program to print the odd and even numbers
for i in range(1, 21):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")

#5. Write a program to print largest number among three numbers.
a, b, c = 1, 25, 16
if a >= b and a >= c:
    print(a, "is the largest")
elif b >= a and b >= c:
    print(b, "is the largest")
else:
    print(c, "is the largest")

#6. Write a program to print even number between 10 and 20 using while
i = 10
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

#7.Write a program to print 1 to 10 using the do-while loop statement.
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break

#8. Write a program to find Armstrong number or not
n= 153
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if sum == n:
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")

#9. Write a program to find the prime or not.
n = 29
if n > 1:
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            print(n, "is not a prime number")
            break
    else:
        print(n, "is a prime number")
else:
    print(n, "is not a prime number")

#10. Write a program to palindrome or not.
n = 121
original = str(n)
reversed_n= original[::-1]

if original == reversed_n:
    print(n, "is a Palindrome")
else:
    print(n, "is not a Palindrome")

#11. Program to check whether a number is EVEN or ODD using switch
n= int(input("Enter a number: "))

if n% 2:
    print("Even")
else:
    print("odd")

#12. Print gender (Male/Female) program according to given M/F using switch
gender = input("Enter M or F: ").strip().upper()

if gender == 'M':
    print("Male")
elif gender == 'F':
    print("Female")
else:
    print("Invalid input")

