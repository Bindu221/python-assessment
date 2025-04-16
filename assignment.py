#Variables DataTypes in Python : it can be Numeric(int, float, complex), Sequence(string, list, tuple), Mapping(dict), Boolean(bool), set(set, frozenset), Binary(bytes, bytearray, memoryview).
x = 21 #numeric - int
y = 2.1 #numeric - float
z = complex(x, y) #numeric - complex
a , b = 'annalect' , "omni" #sequence - string
##################################################
c = """I'm 
learning""" #sequence - multistring
d = '''I'm
good at
making note''' #sequence - multistring
e = [1, 2, "a", True, 2] #list can contain duplicate items, they are mutable, can be modified, replaced, deleted.list is having order for elements(index starts from '0')
print(type(e[2]))
print(type(e[3]))
##################################################################
j = {1: 'python', 2: 'java', 3: 'sql'} #dict is a data structure stores value : key pairs, it is immutable.
print(j)
j2 = dict(a = "python", b = "java", c = "sql") #the keys are case sensitive, keys must be immutable, unique
print(j2)
print(j2["b"])
print(j.get("1"))
j3 = j.keys()
j4 = j2.values()
j2.pop("java")
print(j)
j.popitem()
print(j)
###################################################
k = None
print(bool(k))
k1 = ()
print(bool(k1))
k2 = {}
print(bool(k2))
k3 = 8.8
print(bool(k3))
k4 = 'python'
print(bool(k4))
##########################################################
l = {"a", "b", "c", "a"} #sets are used to store multiple items in a single variable
print(l) #unordered, unchanged, no duplicates allowed(#they are ignored)
#if you keep (True and 1) && (Fasle and 0) in a set they both considered as same in the set
l1 = frozenset(["cat", "rat", "bat"]) #frozenset is an iterable set, no duplicate values are allowed, it's immutable.
print("cat" in l1) 
print("lion" in l1)
fnum = frozenset(l)
print("frozenset obnect is:", fnum)
l2 = {"a", "b", "c", 3, 4}
l3 = (1, 2, 3)
l4 = l2.union(l3)
print(l4)
l2.update(l3)
print(l2)
l5 = l2.difference(l3)
print(l5)
l2.difference_update(l3)
l6 = l2.symmetric_difference(l3)
print(l6)


#####################################################
m = "Bindu"
m1 = bytes(m, 'utf-16')
m2 = memoryview(b"Hello") #memory view shows the buffer
print(m2)
print(m2[0])
print(m2[1])
###########################################################
'''Variable Names
A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.'''

# Legal variable names:
myvar = "mine"
my_var = "mine"
_my_var = "mine"
myVar = "mine"
MYVAR = "mine"
myvar2 = "mine"

# Illegal variable names:

# 2myvar = "John" # SyntaxError
# my-var = "John" # SyntaxError
# my var = "John" # SyntaxError

####################################################################################3
# modules
# A file containing a set of functions you want to include in your application.
# we can import a module
# Random Module
import random
print(random.randint(1, 10))  # Random integer between 1 and 10
print(random.choice(['me', 'myy', 'mine']))  # Random choice from a list
print(random.sample(range(100), 5))

# String Module
import string
print(string.punctuation)
print(string.ascii_letters)
print(string.digits)
##################################################################################33
# Built-In Data Structures:
list = ["lambo", "bugatti", "porsche", "1", "8", "True"]
print(type(list))
print(list[1])
print(list[-1])
print(list[2:5])
list = ["lambo", "bugatti", "porsche", "1", "8", "True"] #Change values
list[2] = "me"
print(list)
list[1:3] = ["me"]
print(list)
list[4:5] = ["mine", 1, 3]
print(list)
list.insert(2, "abcd")
print(list)
list.insert(6,"myy",12345) #can only insert 1 argument
print(list)
list = ["lambo", "bugatti", "porsche", "1", "8", "True"] ## Add List Items
list.append("milkshake")
print(list)

list2 = [1234, 1234, 567, 7890]
list.extend(list2)
print(list)

list.remove("maggie")  # remove list # remove uses values
print(list)

list.pop(3)  # pop uses index
print(list)

del list[1:3]  # can delete with index
print(list)

print(list2)
del list2  # delete the whole list
# print(list2)

list.clear()  # clears the content in the list
print(list)

# looping through list

list3 = ["Bindu", "abc", "qwe", 12345]
print(list3)

for i in list3:
    print(i)

for i in list3:
    if isinstance(i,str):

        print( i.lower())
print(list3)

list4 = ["apple", "banana", "pineapple"]
i = 0
while i < len(list4):
  print(list4[i])
  i = i + 1
[print(x) for x in list3] ##list comprehension

f = list((1, 2, "a", True, 2)) #list can be used as constructor also.
f.append(3)
print("after append:", f) #using append, insert and extend actions in list
f.insert(0, 5)
print("after insert:", f)
f.extend(['no', 6, 7.8])
print("after extend:", f)
f[1] = 23
print(f)
f.remove(23)
print("after remove:", f)
f.pop(0)
print("after pop:", f)
g = [[1, 2, 3]
     [4, 5, 6]
     [7, 8, 9]]
print(g[2][3]) #nested list printing
##############################################################
h = (1, 2, 4) #tuple is immutable
print(type(h))
print(h)
print(h[2])
h[1] = 20 #can't update tuple
print(h)
h1 = (1, 4, 3)
h3 = h1+h
print(h3)
i = ('py', 'txt')
print(h + i) #concatinating 2 tuples
print(h)*3 #repetition of tuples
print(len(h))
###############################################

''' Identify Scenarios where Built-in Structures May Not Work
Dictionaries do not support duplicate keys
Sets do not support indexing
Lists are slow for large data searches (use set or dict for fast lookups)
Tuples are immutable and cannot be modified'''
# remove duplicate from list
list = [1, 2, 2, 3, 4, 4, 5]
unique_list = list(set(list))
print(unique_list)
my_dict = {"a": 1, "b": 2, "c": 2}
unique_values = list(set(my_dict.values()))
print(unique_values)
#####################################################################################3

a = "Bindu is a Quick learner"
b=a.split()
b[2]=""
print(b)

text = "nothing is impossible"
print(text.replace("is", "nothing"))

a="I'm indepndent"
b=" I'm a logical thinker "
print('{} {}'.format(a,b))

a = "hi there this is bindu this is python"
b=a.split(" ")
print(b)
for i in b :
 if len(i)%2==0:
  print(i)
a[::]

'''decorators Function that modifies another function without changing its structure.'''

def my_decorator(func):
    def wrapper():
        print("Something before function executing things")
        func()
        print("Something after function executing things")
    return wrapper

@my_decorator
def say_hello():
    print("Heyy!")
say_hello()

# closure
# Function that remembers variables from its enclosing scope
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(10))
###########################################################################################3

#oops empower the developers to build modular,maintainable and scalable applications
'''classes - defines set of attributes, keyword class
   
   objects - state : ATTRIBUTES REFLECT THE PROPERTIES OF OBJECT
             behaviour: represents the method of an object and reflects the response the object
             identitify: unique name to an object and enables one object to interact with other objects.
  
  inheritance, encapsulation, ploymorphism and abstraction'''

# class
class employee:
    def __init__(self,name,age,job):
        self.name=name
        self.age=age
        self.job=job
    def emp(self):
        print(f"name is {self.name} age is {self.age} job is {self.job}")

obj=employee("Bindu",21,"QA")
obj.emp()
name="BinduB"
age=21
job="QA"
class employe:
    job="dev"
    def emp4(self):
        print(f"name is {name} age is {age} job is {job}")
obj4=employe()
obj4.emp4()

class employee1:
    def emp2(self,name,age,job):
        print(f"name is {name} age is {age} job is {job}")
obj2=employee1()
obj2.emp2("Madhavi",21,"dev")

class employee2:
    name="Madhavi"
    age=21
    job="dev"
    def emp2(self):
        print(f"name is {employee2.name} age is {employee2.age} job is {employee2.job}")
obj2=employee2()
obj2.emp2()

class employee3:
    name="Battina"
    age=21
    job="HR"
    def emp3(self):
        print(f"name is {self.name} age is {self.age} job is {self.job}")
obj3=employee3()
obj3.emp3()

class Hey:
    def __init__(self):
        print("hi bro")
    def add(self,a):
        print("print",a)
    def hi(self,x):
        return x+1
    def __init__(self,name):
        self.name=name
        print(name)
bj=Hey("Bindu")
bj.add(9)
bj.hi(9)

class hola:
    pass
obj= hola()
#assign attributes to the instance of the class
obj.name="Madhavi"
obj.age=22
print(obj.name,obj.age)

class madu:
    def __init__(self,name:str,age:int,sal):
        self.name=name
        self.age =age
        self.sal=sal
    #assert to compare with actual result
        assert age>=21,'age should be greater than 20'
    def id(self):
        return self.age + 100000

    def range(self):
        if self.age>=21 and self.age<=30 :
            print("expected salary = 3000000")
        elif self.age>=31 and self.age<=40 :
            print("expected salary = 6000000")
        elif self.age>=41 and self.age<=50 :
            print("expected salary = 7000000")

obj=madu("Madhavi",35,3030303)
print(obj.id())
obj.rnge()
print(madu.__dict__)

class Miyo:
    @staticmethod
    def isint(num):
        if isinstance(num,float):
            return False
        elif isinstance(num,int):
            return True
        else:
            return False

obj=Miyo()
print(obj.isint(123))
from datetime import date
class Miso:
    name="Miso"
    age=18
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print(self.name + " " +str(self.age))
    @classmethod
    def date(cls,name,age):
        dt=date.today().year
        print(dt)
        return Miso(name,age)
obj=Miso()
obj.display()
# class method
a=Miso.date("Madhavi",34)
a.display()

class employee:
    employeename = "Bindu"

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    @classmethod
    def change_emp_name(cls, new_name):
        cls.employeename = new_name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    def deposit(self, amount):
        if employee.is_valid_amount(amount):
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount!")


account = employee("honey", 5000)
print("employee name:", employee.employeename)
account.deposit(100)
account.deposit(-50)
employee.change_emp_name("milky")
print("Updated emp name:", employee.employeename)
#############################################################################################
# type casting
from datetime import datetime
today = datetime.now()
date_str = today.strftime("%Y-%m-%d")
print(date_str)
num_str = "123"
num_int = int(num_str)
num_str = "123"
num_int = int(num_str)
num = 100
num_float = float(num)
#################################################################################

# """Python Conditions and If statements
# Python supports the usual logical conditions from mathematics:
# Usage of if statement for various built-in structures
# Using if with list

lst = [1, 2, 3]
if lst:  # Checks if list is non-empty
    print("List is not empty")

dct = {} # Using if with dictionary
if not dct:  # Checks if dictionary is empty
    print("Dictionary is empty")

string = "Python" # Using if with string
if "P" in string:
    print("String contains 'P'")

tpl = () # 2) Usage of if-else statement for various built-in structures
if tpl: # If-else with a tuple
    print("Tuple is not empty")
else:
    print("Tuple is empty")

s = {1, 2, 3}
# If-else with set
if 2 in s:
    print("Set contains 2")
else:
    print("Set does not contain 2")

''' While loop and its importance in implementation. While loops are useful when the number of iterations is unknown and depends on a condition. Printing numbers using while loop'''
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1

# 4) Accept a file as user input, count words, unique words, and letters
filename = input("Enter file name: ")
with open(filename, 'r') as f:
    text = f.read()

words = text.split()
unique_words = set(words)
letters = len(text.replace(" ", "").replace("\n", ""))

print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Total letters: {letters}")


'''Count Occurrences of a Word in a File'''
word_to_find = input("Enter the word to count: ")
with open("Omni Assist - Google.txt", 'r') as f:
    text = f.read()
count = text.split().count(word_to_find)
print(f"The word '{word_to_find}' appears {count} times.")

# 6) Operator Overloading and Its Importance. Operator overloading allows us to redefine how operators like +, -, etc., work for custom objects.
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):  # Overloading +
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)
print(v1 + v2)  # Output: (6, 8)

# Key Takeaway: Helps in making custom classes behave like built-in types.7) Functions as First-Class Objects
# Functions in Python can be assigned to variables, passed as arguments, and returned from other functions.
def greet(name):
    return f"Hello, {name}"

g = greet  # Assigning function to a variable
print(g("Mine"))  # Hello, kan

def execute_func(func, name):
    return func(name)

print(execute_func(greet, "Bindu"))  # Hello, kannan

# 8) Object References, Their Advantages, and Why They Are Needed
# In Python, variables store references to objects, not actual data.

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Bindu")
p2 = p1  # p2 now references the same object as p1

print(p2.name)  # Alice
p1.name = "Btch"
print(p2.name)  # Bob (both reference the same object)
# Advantages: Saves memory, enables object sharing.

# 9) Find Min & Max Count in a DataFrame

import pandas as pd

df = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [5, 15, 25, 35]})
print(f"Min count: {df.count().min()}")
print(f"Max count: {df.count().max()}")

# 10) Find Max and Min Value for a Specific Column
print(f"Max in column A: {df['A'].max()}")
print(f"Min in column A: {df['A'].min()}")

# 11) Find Duplicate Rows and Their Count from Multiple Tables python Copy code

df2 = pd.DataFrame({'A': [10, 10, 20, 30], 'B': [5, 5, 15, 25]})
duplicates = df2[df2.duplicated()]
print("Duplicate rows:\n", duplicates)
print("Duplicate count:", duplicates.shape[0])

# Find List of Columns w.r.t Data Type
print(df.dtypes)

# 13) Find Unique Values from a Table Attribute
print(df['A'].unique())

# 14) Find List of Rows w.r.t Data Type
for dtype in df.dtypes.unique():
    print(f"Rows with data type {dtype}:\n", df.select_dtypes(include=[dtype]))

# 15) Find Missing Values from the Table
df_missing = pd.DataFrame({'A': [1, 2, None], 'B': [None, 5, 6]})
print(df_missing.isnull().sum())  # Count of missing values per column
#############################################################################################
'''Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# WHILE LOOP
while True:
    user_input = input("Enter a number (type 'exit' to stop): ")
    if user_input.lower() == "exit":
        break
    print(f"You entered: {user_input}")
##############################################################################################3

'''Try Except
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.'''
try:

    print(x)
except:
    print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

x = -1
if x < 0:
  raise Exception("Sorry, no numbers below zero")
x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")
# Built-in Math Functions
x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
x = abs(-7.25)
print(x)
x = pow(4, 3)
print(x)

import math

x = math.sqrt(64)
print(x)

import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x)  # returns 2
print(y)  # returns 1
x = math.pi
print(x)
#################################################################################################################3
# class
#
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce(self):
    return f"My name is {self.name}, and I am {self.age} years old."


person1 = Person("Alice", 25)
print(person1.introduce())


# TXT File: Open, Read, Write
with open("kannan.txt", "w") as file:
  file.write("Hello, this is a sample text file.\n")
  file.write("Python makes file handling easy.")

with open("kannan.txt", "r") as file:
    content = file.read()
    print(content)

with open("kannan.txt","a") as file:
  file.write("\nAppending new data to the file.")

'''JSON File: Open, Read, Write
Python provides the json module for handling JSON files'''

import json
data = {
    "name": "Alice",
    "age": 25,
    "skills": ["Python", "Machine Learning"]
}

with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)

loaded_data["age"] = 26  # Updating age
with open("data.json", "w") as file:
    json.dump(loaded_data, file, indent=4)

with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)

'''Parquet File: Open, Read, Write
Parquet is a columnar storage format optimized for big data. Python’s pandas library can handle Parquet files.'''
import pandas as pd

data = {"Name": ["Alice", "Bob"], "Age": [25, 30]}
df = pd.DataFrame(data)

df.to_parquet("data.parquet", engine="pyarrow")

df = pd.read_parquet("data.parquet", engine="pyarrow")
print(df)
#####################################################################################################################33

























