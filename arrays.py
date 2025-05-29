#1.Write a function to add integer values of an array
def sum_array(arr):
    return sum(arr)
if __name__ == "__main__":
    input_str = input("Enter integers separated by spaces: ")
    arr = list(map(int, input_str.strip().split()))
    total = sum_array(arr)
    print("Sum of array elements:", total)

#2. Write a function to calculate the average value of an array of integers
def avg_array(arr):
    return sum(arr) / len(arr) if arr else 0
if __name__ == "__main__":
    input_str = input("Enter integers separated by spaces: ")
    arr = list(map(int, input_str.strip().split()))
    avg = avg_array(arr)
    print("Average of array elements:", avg)

#3. Write a program to find the index of an array element
def find_index(arr, value):
    try:
        return arr.index(value)
    except ValueError:
        return -1
if __name__ == "__main__":
    input_str = input("Enter integers separated by spaces: ")
    arr = list(map(int, input_str.strip().split()))
    value = int(input("Enter the value to find its index: "))
    index = find_index(arr, value)
    if index != -1:
        print(f"The index of {value} is: {index}")
    else:
        print(f"{value} not found in the array.")

#4.Write a function to test if array contains a specific value
arr = [4,15,45,40,50]
for n in arr:
    if n == 5:
        print("Element exist")
#5. # Write a function to remove a specific element from an array.
arr = [44,55,10,15,19,5,4]
arr.remove(10)
print(arr)

#6.Write a function to copy an array to another array
arr = ['p','y','t','h','o','n']
arr1 = [] 
arr1 = arr.copy() 
print(arr1)

#7.Write a function to insert an element at a specific position in the array
arr = [11,31,41,51,61,71,81,91]
arr.insert(1,23)
print(arr)

#8.Write a function to find the minimum and maximum value of an array
arr = [100,3,300,20,500,999,1001,1007]
minposition = arr.index(min(arr))
print ("The minimum is at position:", minposition)

#9. Write a function to reverse an array of integer values
arr = [29,4,5,9,12]
arr.reverse()
print(arr)

#10. Write a function to find the duplicate values of an array
arr = [21,41,21,12,10]
for i in range(0,len(arr)):
    for k in range(i + 1,len(arr)):
        if arr[i] == arr[k]:
            print("Duplicate element in given array:",arr[k])

#11. Write a program to find the common values between two arrays
arr = ['c','a','r','e','e','r']
arr1 = ['s','a','r']
print("Common values in given arrays:",set(arr).intersection(arr1))

#12. Write a method to remove duplicate elements from an array
def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
arr = [1, 2, 2, 3, 4, 3, 5]
print(remove_duplicates(arr)) 

#13. Write a method to find the second largest number in an array
def find_second_largest(arr):
    if len(arr) < 2:
        return None  
    first = second = float('-inf')
    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    return second if second != float('-inf') else None
arr = [10, 20, 4, 45, 99, 99]
print(find_second_largest(arr))

#14. Write a method to find the second largest number in an array
arr = [10, 20, 4, 45, 99, 99]
result = find_second_largest(arr)
print("Second largest number is:", result)
#15. Write a method to find number of even number and odd numbers in an array
def count_even_odd(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
arr = [1, 2, 3, 4, 5, 6, 7]
even, odd = count_even_odd(arr)
print("Even numbers:", even)  
print("Odd numbers:", odd)    

#16. Write a function to get the difference of largest and smallest value
def max_min_difference(arr):
    if not arr:
        return None 
    largest = max(arr)
    smallest = min(arr)
    return largest - smallest
arr = [5, 1, 9, 6, 7]
result = max_min_difference(arr)
print("Difference between largest and smallest:", result) 
#17. Write a method to verify if the array contains two specified elements(12,23)
def contains_elements(arr, elem1=12, elem2=23):
    return elem1 in arr and elem2 in arr
arr1 = [5, 12, 7, 23, 9]
arr2 = [12, 5, 8, 10]
print(contains_elements(arr1))  
print(contains_elements(arr2))  


#18. Write a program to remove the duplicate elements and return the new array
def remove_duplicates(arr):
    seen = set()
    unique_arr = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            unique_arr.append(item)
    return unique_arr
arr = [1, 2, 2, 3, 4, 4, 5]
new_arr = remove_duplicates(arr)
print("New array without duplicates:", new_arr)

