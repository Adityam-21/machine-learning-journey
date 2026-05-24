#VARIABLES AND DATA TYPES:

name = "Adi"  # variable name is assigned a string value "Adi"
print(type(name) == str)  # way of checking if the variable is a string
print(
    isinstance(name, str)
)  # another way of checking if the variable is a string wether name is an istance of the string class


age = float(
    "25"
)  # variable age is assigned a float value by converting the string "25" to a float
print(
    isinstance(age, float)
)  # checking if the variable age is an instance of the float class

data = [10, 20, 30, 40, 50]  # variable data is assigned a list of integers
for value in data:
    if value > 25:  # checking if the value is greater than 25
        print(value)  # if the condition is true, it prints the value

name = "Adi"
name += "Is a great guy"
print(name.split()) # String Methods

name = 'Adityam'
print(name[1:4])

##CONDITIONAL STATEMENTS:

#ENUMS
from enum import Enum 

class Stage(Enum):# creating an enumeration class called Stage
    LOADING = 1 # defining a member of the enumeration called LOADING with a value of 1
    PROCESSING = 2
    COMPLETED = 3
    
current_stage = Stage.LOADING # assigning the value of Stage.LOADING to the variable current_stage
print(current_stage)

#LISTS:

items = ["Adi" , "Raj" , "Sita" , "gita"] # creating a list of items

new_items = sorted(items, key=str.lower) # sorting the list of items in a case-insensitive manner using the sorted function and passing the str.lower function as the key argument
print(new_items) # printing the sorted list of items to show that it has been sorted in a case-insensitive manner
print(items) # printing the original list of items to show that it has not been modified by the sorted function

#TUPLES:

names = ("Adi", "Raj", "Sita", "Gita") # creating a tuple of names
new_names = sorted(names) # sorting the tuple of names using the sorted function
print(new_names) # printing the sorted list of names to show that it has been sorted in a case-sensitive manner
print(names)

#DICTIONARIES:

person = {"name": "Adi", "age": 25, "city": "New York"} # creating a dictionary representing a person with keys "name", "age", and "city"
print(person.get("name" , "city")) # using the get method to retrieve the value associated with the key "name" in the person dictionary
print(person.update({"city": "Los Angeles"})) 