# # Numpy helps the array object which is far better than lists
# # The array object in NumPy = ndarray, gives supporting functions and make the work easy with ndarray
# # Arrays are very frequently used in data science, where speed and resources are very important.

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
arr = np.array(42)
print(arr)
arr = np.array([[1, 2, 3], [4, 5, 6]]) # Creating a 2-D array containing two arrays with the values 1,2,3 and 4,5,6:
print(arr)
# 3-D arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #array having 2-D arrays (matrices) called 3-D array.
print(arr)

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[2] + arr[3])
# Access 2-D Arrays

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[1, 1, 2])
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])
print(arr[1:5])
print(arr[4:])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])
print(arr[1:5:2])
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
print(arr[0:2, 1:4])
print(arr.dtype)
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)
import numpy as np

arr = np.array(['a', '2', '3'], dtype='i')
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)
arr = np.array([1, 2, 3, 4, 5])
x = arr.view() #Make a view, change the view, and display both arrays:
arr[0] = 42
x[0] = 31
print(arr)
print(x)
print(arr.shape)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
newarr = arr.reshape(2, 3, 2)
print(newarr)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)
# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
#
# We can use reshape(-1) to do this.

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)
arr = np.array([1, 2, 3])
for x in arr:
  print(x)
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
      print(x)
for x in arr:
  for y in x:
    print(y)
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)
for x in arr:
  for y in x:
    for z in y:
      print(z)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)   # Element-wise addition
print(a * b)   # Element-wise multiplication
print(a ** 2)  # Square each element
print(np.sum(arr))     # Sum of all elements
print(np.mean(arr))    # Mean (average)
print(np.min(arr))     # Minimum value
print(np.max(arr))     # Maximum value
print(np.std(arr))     # Standard deviation
arr = np.array([1, 2, 3, 4, 5, 6,7])
newarr = np.array_split(arr, 5)
print(newarr)
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)
import numpy as np
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

###############################################################################
# # What is a Series?
# # A Pandas Series is like a column in a table.
# #
# # It is a one-dimensional array holding data of any type.
import pandas as pd
#
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)
data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}
# load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
print(df.loc[0])
print(df.loc[[0, 1]])
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
print(df.loc["day2"])
df = pd.read_csv('data.csv')
print(df)
print(df.to_string())
pd.options.display.max_rows = 9999
df = pd.read_csv('data.csv')
print(df)
print(df.head())
print(df.head(10))
new_df = df.dropna()
print(new_df.to_string())
df.dropna(inplace = True)
print(df.to_string())
df.fillna(130, inplace = True)
df["Calories"].fillna(130, inplace = True)
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df["Calories"].fillna(x, inplace = True)
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)
import pandas as pd
df = pd.read_csv('data.csv')
print(df.head())
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())
# Replacing Values
df.loc[7, 'Duration'] = 45
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
# duplicates
print(df.duplicated())
# Removing Duplicates
# To remove duplicates, use the drop_duplicates() method.
df.drop_duplicates(inplace = True)
# df.corr()
############################################################################################################33333
'''PySpark Tutorial for Beginners 🚀
PySpark is the Python API for Apache Spark, an open-source distributed computing framework used for big data processing and analytics. This tutorial will introduce you to PySpark and help you get started.
.What is PySpark?
PySpark is the Python API for Apache Spark.
It allows data engineers and data scientists to process large datasets efficiently.
It supports distributed computing and can be used for data processing, machine learning, and real-time analytics.'''
# pip install pyspark
import pyspark
print(pyspark.__version__)
#  Creating a PySpark Session
# A SparkSession is the entry point for using PySpark. It allows you to create and manipulate DataFrames.
from pyspark.sql import SparkSession
# Create a Spark session
spark = SparkSession.builder.appName("PySparkTutorial").getOrCreate()
# Check the Spark session
print(spark)
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)
df.show()
df = spark.read.csv("data.csv", header=True, inferSchema=True)
df.show()
# 3️⃣ Basic DataFrame Operations
# a) Show & Describe Data
df.show(5)  # Show first 5 rows
df.printSchema()  # Print DataFrame schema
df.describe().show()  # Get summary statistics
# b) Selecting & Filtering
df.select("name", "age").show()  # Select specific columns
df.filter(df.age > 25).show()  # Filter rows where age > 25
# Grouping & Aggregation
df.groupBy("age").count().show()  # Count occurrences of each age
df.agg({"age": "max"}).show()  # Get max age
# SQL Queries in PySpark
df.createOrReplaceTempView("people")
result = spark.sql("SELECT name, age FROM people WHERE age > 25")
result.show()
# Working with Missing Data
df.na.drop().show()  # Drop rows with missing values
df.na.fill("Unknown").show()  # Fill missing values with "Unknown"
# Saving Data
df.write.csv("output.csv", header=True)  # Save as CSV
df.write.parquet("output.parquet")  # Save as Parquet format
# Closing Spark Session
spark.stop()
############################################################################################
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





































