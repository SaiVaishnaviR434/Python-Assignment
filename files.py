file1 = open("HW.txt","r")
data = file1.read()
print(data)
print()

file2 = open("Blank.txt","w")
str1 = 'Python'
file2.write(str1)
print()

file3 = open("HW.txt","r+")
print(file3.readline(11))
print()
