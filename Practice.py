""" 


# Python functions
#
#
#def my_function(fname):
#    print(fname+ ' Tungwa')
#my_function("Rashid")
#my_function("Bakari")
#my_function("Hasaan")

#Function with many arguments
def my_func(fname,lname):
    print(fname +" "+lname)
my_func("John","Doe")

#Arbitrary arguments
def my_function(*kids):
    print("The youngest child is" + kids[2])
my_func("emily","joy")

#Default parameter value
def my_func(country="Kenya"):
    print(f'I am from '+ country)
my_func("sudan")
my_func("somalia")
my_func()
my_func("egypt")

# PASSING A LIST AS AN ARGUMENT
def my_func(food):
    for x in food:
        print(x)
fruits = ["cherry","mango","orange"]
my_func(fruits)



# RETURN VALUES


def my_func(x):
    return 5*x
print(my_func(3))
print(my_func(5))
print(my_func(9))

#PASS Statement

def my_func():
    pass #since function definition cannot be empty, the pass statement removes the error message and the function can be exercuted

# Lambda Functin
x = lambda a,b: a * b
print(x(5,6))

# Lambda function with multiple arguments
def my_func(x,y):
    return lambda a,b: a * b + x + y
print(my_func(5,6)(2,3))  # Output: 2*3 + 5 + 6 = 17
# Lambda function with multiple arguments and default values
def my_func(x=1,y=2):
    return lambda a,b: a * b + x + y    
print(my_func(5,6)(2,3))  # Output: 2*3 + 5 + 6 = 17

#PYTHON ARRAYS
#USING LIST AS ARRAYS
cars = ["toyota","nissan","mazda","honda"]
print(cars[0])  # Accessing the first element
print(cars[1])  # Accessing the second element
print(cars[2])  # Accessing the third element
print(len(cars))  # Getting the length of the list
# Adding an element to the list
cars.append("subaru")
print(cars)  # Displaying the updated list

#looping array elements
for x in cars:
    print(x)


# PYTHON OBJECT ORIENTED PROGRAMMING
class MyClass:
    x = 5 * 20
p1 = MyClass()
print(p1.x)


# THE __init__() FUNCTION
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 =  Person('john',23)
print('The name is ' + p1.name)
print('The age is ' + str (p1.age))

# THE __str__() FUNCTION
# STRING REPRESENTATION OF AN OBJECT WITHOUT USING THE __str__() FUNCTION
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 =  Person('john',23)
print(p1)
#
#

#
#

# STRING REPRESENTATION OF AN OBJECT WITH THE __str__() FUNCTION
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f'{self.name} ({self.age})'
p1 =  Person('john',23)
print(p1)

# OBJECT METHODS
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myFunction(self):
        print(f'Hello my name is ' + self.name)
p1 = Person ('john',36)
p1.myFunction()
 """
# 