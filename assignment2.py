####################################################
from datetime import datetime

unique_id = "LP" + datetime.now().strftime("%Y%m%d%H%M%S") # Learning progress tracker starts now

learning_progress = {
    "id": unique_id,
    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "topics": {
        "Python Basics": 80,
        "SQL": 60,
        "Automation Testing": 75,
        "Data Quality": 40
    }
}
print(f"Session ID: {learning_progress['id']}")
print(f"Created At: {learning_progress['created_at']}")
print("Learning Topics Progress:")
for topic, percent in learning_progress["topics"].items():
    print(f"  - {topic}: {percent}%")

####################################################################################
from datetime import date

# Date to String
today = date.today()
today_str = str(today)

# String to Integer
str_num = "123"
int_num = int(str_num)

# Integer to String
num = 143
num_str = str(num)

# Integer to Float
int_val = 10
float_val = float(int_val)
###################################################

# Only dictionary fits here
student_marks = {
    "Rahul": 85,
    "Priya": 90,
    "Amit": 78
}
# can't print with list/tuple/set directly
print("Rahul's marks:", student_marks["Rahul"])

# Duplicates automatically
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print("Unique Emails:", emails)  # 'a@gmail.com' will print again

# order matters!
steps = ["Boil water", "Add pasta", "Stir", "Drain"]
steps.append("Serve")  # You can add or change steps
print("Recipe steps:", steps)

# Storing coordinates of a location – fixed and read-only
location = (28.6139, 77.2090)  # (Lat, Long)
print("Location:", location) # location[0] = 30.0 Not allowed
#########################################################################

# List
dup_list = [1, 2, 2, 3, 4, 4]
no_dupes = list(set(dup_list))

# Set already removes duplicates
my_set = set(dup_list)

# Dictionary – remove duplicate values (not keys)
sample_dict = {"a": 1, "b": 2, "c": 1}
unique_values = list(set(sample_dict.values()))
###########################################################3

# Valid naming
my_variable = 10

# Breaking rules - invalid variable names
# 2cool = 5 invalid syntax
# my-var = 10 can't use '-' in variable name
# class = "test" 'class' is a reserved keyword
##########################################################################3
# list
print("🔹 List Example:")
my_list = [1, 2, 3]
print("Original List:", my_list)
my_list.append(4)
print("After append:", my_list)
my_list[1] = 20
print("After modifying index 1:", my_list)
my_list.remove(3)
print("After removing 3:", my_list)

#tuple
print("\n🔹 Tuple Example:")
my_tuple = (10, 20, 30)
print("Original Tuple:", my_tuple)
print("Accessing index 1:", my_tuple[1])
# my_tuple[1] = 99  #Tuples are immutable

#set
print("\n🔹 Set Example:")
my_set = {1, 2, 3}
print("Original Set:", my_set)
my_set.add(4)
print("After adding 4:", my_set)
my_set.update([5, 6])
print("After updating with [5, 6]:", my_set)
my_set.remove(2)
print("After removing 2:", my_set)

#Dictionary 
print("\n🔹 Dictionary Example:")
my_dict = {"name": "Aman", "age": 22}
print("Original Dict:", my_dict)
my_dict["city"] = "Delhi"
print("After adding 'city':", my_dict)
my_dict["name"] = "Rahul"
print("After modifying 'name':", my_dict)
del my_dict["age"]
print("After deleting 'age':", my_dict)
########################################################################

my_string = "  Hello, World!  "
# Concatenation
concat = my_string + " Let's learn Python."
# Replace
replaced = my_string.replace("World", "Bhai")
# Trim
trimmed = my_string.strip()
# Other common ops
upper = my_string.upper()
lower = my_string.lower()
split_words = my_string.split(",")
############################################################3

import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM my_table")
rows = cursor.fetchall()
columns = [description[0] for description in cursor.description]
print("Rows:", len(rows))
print("Columns:", len(columns))
######################################################################

'''-- Assuming we have table1 and table2 From table1'''
# SELECT col1, COUNT(*)
# FROM table1
# GROUP BY col1
# HAVING COUNT(*) > 1;

# -- Across table1 and table2
# SELECT col1, COUNT(*) 
# FROM (
#     SELECT col1 FROM table1
#     UNION ALL
#     SELECT col1 FROM table2
# ) AS combined
# GROUP BY col1
# HAVING COUNT(*) > 1;

#####################################################################333