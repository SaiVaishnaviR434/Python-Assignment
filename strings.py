#1. Different ways creating a string
s1 = "Bright IT"
s2 = str("Career")
s3 = """This is
a multiline
string"""
print(s1, s2)
print(s3)

#2. Concatenating two strings using + operator
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

#3. Finding the length of the string
s = "Hello World"
print(len(s))

#4. Extract a string using Substring
s = "Bright IT Career"
substring = s[0:5]  
print(substring)

#5. Searching in strings using index()
s = "Bright Career"
pos = s.index("Career")  
print(pos)

#6. Matching a String Against a Regular Expression With matches()
import re
s = "Hello123"
if re.match(r"Hello\d+", s):
    print("Matched")
else:
    print("Not Matched")

#7. Comparing strings
s1 = "apple"
s2 = "banana"
print(s1 == s2)        
print(s1 < s2)         

#8. startsWith(), endsWith() and compareTo()
s = "OpenAI GPT"
print(s.startswith("Open"))  
print(s.endswith("GPT"))      
print("apple" < "banana")     


#9. Trimming strings with strip()
s = "   Hello World   "
trimmed = s.strip()
print(trimmed)

#10. Replacing characters in strings with replace()
s = "Hello World"
new_s = s.replace("World", "Python")
print(new_s)


#11. Splitting strings with split()
s = "apple,banana,cherry"
fruits = s.split(",")
print(fruits)


#12. Converting integer objects to Strings
num = 123
str_num = str(num)
print(str_num, type(str_num))


#13. Converting to uppercase and lowercase
s = "Hello World"
print(s.upper())  
print(s.lower())   
