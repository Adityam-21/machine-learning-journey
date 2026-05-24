#FUNCTIONS:

def stats (a,b):
    return a + b, a - b 
result = stats(10, 5)
print(result) # prints the result of the stats function, which is a tuple containing the sum and difference of 10 and 5
sum_result, difference_result = stats(10, 5) # unpacks the tuple returned

#VARIABLE SCOPE:
#(LEGB RULE: Local, Enclosing, Global, Built-in)
x = 50 # global variable x is assigned the value 50

def outer(): 
    x = 20
    
    def inner():
        x = 10 # local variable x is assigned the value 10, which is different from the global variable x defined outside the function
        print(x)
        
    inner()
    
outer() # calling the outer function, which in turn calls the inner function and prints the value of x defined in the inner function (10)
    
#NESTED FUNCTIONS:

def outer(a):
    def inner(b):
        return a + b # the inner function takes an argument b and returns the sum of a and b, where a is a variable defined in the outer function
    return inner

func = outer(5) # calling the outer function with the argument 5, which returns the inner function. The returned inner function is assigned to the variable func
print(func(3)) # calling the outer function with the argument 5, which returns the inner function. Then, calling the returned inner function with the argument 3, which adds 5 and 3 and returns the result (8)
    
#LOOPS:

# for loop
nums = [10, 20, 30] 

for num in nums: 
    print(num)
    
i = 0

# while loop
while i < 5:
    print(i)
    i += 1

#LIST COMPREHENSIONS:
nums = [1 , 2 , 3 , 4]

evens = [x for x in nums if x % 2 == 0] # using a list comprehension to create a new list called evens that contains only the even numbers from the original list nums
print(evens) # printing the list of even numbers to show that it contains only the even numbers from the original list nums 

#Enumerate function:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits): # using the enumerate function to loop through the list of fruits and get both the index and the value of each fruit
    print(index, fruit) # printing the index and the corresponding fruit to show how the enumerate function works
    
# ZIP function:
names = ["Adi", "Raj", "Sita"]
ages = [25, 30, 35]
for name, age in zip(names, ages): # using the zip function to loop through both the names and ages lists simultaneously and get the corresponding name and age for each iteration
    print(name, age) # printing the name and age to show how the zip function works