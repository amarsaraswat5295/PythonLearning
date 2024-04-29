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


# decorators

def decorator(func):
    def wrapper():
        print("This is printed before the function is called")
        func()
        print("This is printed after the function is called")

    return wrapper


@decorator
def say_hello():
    print("Hello! The function is executing")


# say_hello = decorator(say_hello)


@decorator
def say_hi():
    print("Hi! The function is executing")


# say_hi = decorator(say_hi)


say_hello()
say_hi()


# use of *args (variable-length arguments)

def total_sum_numbers(*args):
    total = 0
    for number in args:
        total += num
    return total


print(total_sum_numbers(1, 2, 3, 4, 5))


# use of **kwargs (keyword arguments)

def my_fun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
my_fun(first='Geeks', mid='for', last='Geeks')


# object-oriented programming

class car:
    def __init__(self, model_name, year):
        self.model_name = model_name
        self.year = year

    def display(self):
        print(self.model_name, self.year)


c1 = car("Toyota", 2016)
c1.display()


# Whenever a class is instantiated __new__ and __init__ methods are called.
# __new__ method will be called when an object is created and
# __init__ method will be called to initialize the object.

class A(object):
    # new method returning a string
    def __new__(cls):
        print("object created")
        return "return object"


print(A())


# inheritance
# superclass
class Animal:
    def speak(self):
        return "I am an animal."


# subclass inheriting from Animal

class Dog(Animal):
    def bark(self):
        return "Woof!"


# Creating an instance of Dog
my_dog = Dog()

# Accessing method from superclass
print(my_dog.speak())  # subclass inheriting from Animal

# Accessing method from subclass
print(my_dog.bark())  # Output: Woof!


# multiple inheritance


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Employee:
    def __init__(self, emp_id, salary):
        self.emp_id = emp_id
        self.salary = salary

    def work(self):
        print("I am working hard to meet deadlines.")


class Manager(Person, Employee):
    def __init__(self, name, age, emp_id, salary):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)

    def manage(self):
        print("I am managing a team.")


# Create an instance of Manager
manager = Manager("John", 35, "M001", 60000)

# Call methods inherited from Person
manager.greet()  # Output: Hello, my name is John and I am 35 years old.

# Call methods inherited from Employee
manager.work()  # Output: I am working hard to meet deadlines.

# Call method specific to Manager
manager.manage()  # Output: I am managing a team.


# Multilevel Inheritance

class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    def bark(self):
        print("Dog barks")


class GermanShepherd(Dog):
    def guard(self):
        print("German Shepherd guards")


# Create instances of each class
animal = Animal()
dog = Dog()
german_shepherd = GermanShepherd()

# Call methods from each class
animal.speak()  # Output: Animal speaks
dog.speak()  # Output: Animal speaks
dog.bark()  # Output: Dog barks
german_shepherd.speak()  # Output: Animal speaks
german_shepherd.bark()  # Output: Dog barks
german_shepherd.guard()  # Output: German Shepherd guards


# Hierarchical Inheritance:

class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("Woof!")


class Cat(Animal):
    def speak(self):
        print("Meow!")


class Cow(Animal):
    def speak(self):
        print("Moo!")


# Create instances of subclasses


dog = Dog()
cat = Cat()
cow = Cow()

# Call speak method of each subclass
dog.speak()  # Output: Woof!
cat.speak()  # Output: Meow!
cow.speak()  # Output: Moo!


# overriding concept

class DataModel:
    def evaluate(self, predictions, true_values):
        print("Evaluating model...")
        # Implementation of a basic evaluation metric


class ClassificationModel(DataModel):
    def evaluate(self, predictions, true_values):
        print("Evaluating classification model...")
        # Implementation of classification-specific evaluation metrics, e.g., accuracy, F1 score


class RegressionModel(DataModel):
    def evaluate(self, predictions, true_values):
        super().evaluate("no",2)
        print("Evaluating regression model...")
        # Implementation of regression-specific evaluation metrics, e.g., MSE, RMSE


regression_model=RegressionModel()
regression_model.evaluate("yes",1)
