# Find the Factorial of a Number.

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact


num = 5
print("Factorial of", num, "is",
      factorial(num))


# Python program to find the maximum of two numbers
def maximum_of_two_numbers(num1, num2):
    if num1 >= num2:
        return num1
    else:
        return num2


# Driver code
num1 = 2
num2 = 4
print(maximum_of_two_numbers(num1, num2))


# Python3 program to swap first and last element of a list

# Swap function
def swap_list_elements(new_list):
    new_list[0], new_list[-1] = new_list[-1], new_list[0]
    return new_list


# Driver code
new_list = [12, 35, 9, 56, 24]
print(swap_list_elements(new_list))


# function which return reverse of a string
def is_palindrome(name):
    return name == name[::-1]


# Driver code
name = "amar"
print(is_palindrome(name))

for x in range(6):
    print(x)
else:
    print(0)

# list in python

my_list = [10, 20, 30, 40, 50]
my_list[2] = 35  # Updating the third element
my_list.append(40)  # adding element to the last
my_list.insert(1, 15)  # Inserting 15 at index 1
my_list.remove(30)  # Removing the value 30
my_list.pop(2)  # Removing the element at index 2

# tuple

# Creating a tuple
my_tuple = (1, 2, 'three', 4.0)

# Accessing elements using indexing
first_element = my_tuple[0]
second_element = my_tuple[1]
third_element = my_tuple[2]
fourth_element = my_tuple[3]

# Printing the elements
print("First element:", first_element)
print("Second element:", second_element)
print("Third element:", third_element)
print("Fourth element:", fourth_element)

# Two tuples to be concatenated
tuple1 = (1, 2, 3)
tuple2 = ('four', 'five', 'six')

# Concatenating the two tuples
concatenated_tuple = tuple1 + tuple2

# Printing the concatenated tuple
print("Concatenated Tuple:", concatenated_tuple)


# lambda function

def max(a, b):
    return lambda a, b: a if (a > b) else b


print(max(1, 2))
