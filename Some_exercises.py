



# Using an os function / getting the current directory
# os.getcwd()
# work_dir = os.getcwd()

# Changing directory
# os.chdir("/home/georgeboorman")

# Get the local environment
# os.environ

# Import multiple functions from a module
# from os import chdir, getcwd
# No need to include os.
# getcwd()

'''with pandas : .mean() method to find the average order value.'''

# Read in sales.csv
# sales_df = pd.read_csv("sales.csv")

# # Print the mean order_value
# print(sales_df["order_value"].mean())

# # Print the total value of sales
# print(sales_df["order_value"].sum())

######################################################
######################################################
######################################################

# Create the clean_string function
def clean_string(text):
  
  # Replace spaces with underscores
  no_spaces = text.replace(" ", "_")
  
  # Convert to lowercase
  clean_text = no_spaces.lower()
  
  # Return the final text as an output
  return clean_text

converted_text = clean_string("I LoVe dATaCamP!")
print(converted_text)

######################################################
######################################################
######################################################

# # Create the convert_data_type function
# def convert_data_structure(data, data_type="list"):
#   # Add a multi-line docstring
#   """
#   Convert a data structure to a list, tuple, or set.
  
#   Args:
#   	data (list, tuple, or set): A data structure to be converted.
#     data_type (str): String representing the type of structure to convert data to.
    
#   returns:
#   	data (list, tuple, or set): Converted data structure.
#   """
#   if data_type == "tuple":
#     data = tuple(data)
#   elif data_type == "set":
#     data = set(data)
#   else:
#     data = list(data)
#   return data

# print(help(convert_data_structure))

######################################################
######################################################
######################################################
# def concat(**kwargs):
  
#   # Create an empty string
#   result = ""
  
#   # Iterate over the Python kwargs
#   for kwarg in kwargs.values():
#     result += " " + kwarg
#   return result

# # Call the function
# print(concat(a="Python", b="is", c="great!"))

######################################################
######################################################
######################################################
''' Lambda '''

sale_price = 29.99

# Define a lambda function called add_tax
add_tax = lambda x: x*1.2

# Call the lambda function
print(add_tax(sale_price))

'''------------------------------------------'''

sale_price = 29.99

# Call a lambda function adding 20% to sale_price
print((lambda x: x*1.2)(sale_price))
''' you can call directly after the lambda function'''

'''------------------------------------------'''

''' Lambda functions with iterables '''
sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]

# Create add_taxes to add 20% to each item in sales_prices
add_taxes = map(lambda x: x*1.2, sales_prices)

# Create the updated list, sales_plus_tax / list is for print the result
sales_plus_tax = list(add_taxes)

# Print the new list with updated values
print(sales_plus_tax)

######################################################
######################################################
######################################################
''' try-except : don't block the rest of the code -- raise : block completely '''

# def snake_case(text):
#   # Attempt to clean the text
#   try:
#     # Swap spaces for underscores
#     clean_text = text.replace(" ", "_")
#     clean_text = clean_text.lower()
#   # Run this code if an error occurs
#   except:
#     print("The snake_case() function expects a string as an argument, please check the data type provided.")
    
# snake_case("User Name 187")

'''------------------------------------------'''

# def snake_case(text):
#   # Check the data type
#   if type(text) == str: # if isinstance(values, (list, set)):  # ✅ Most Pythonic
#     clean_text = text.replace(" ", "_")
#     clean_text = clean_text.lower()
#   else:
#     # Return a TypeError error if the wrong data type was used
#     raise TypeError("The snake_case() function expects a string as an argument, please check the data type provided.")
    
# snake_case("User Name 187")

######################################################
######################################################
######################################################

# print("h32rb1r7".index("r"))

# The .index() method returns 3 because the first occurrence of the character "r" is at index 3.
'''------------------------------------------'''
# ip_addresses = "192.168.140.81, 192.168.109.50, 192.168.243.140"
# print(ip_addresses.index("192.168.243.140"))
# 'response 32'


######################################################
######################################################
######################################################

'''enumerate '''

# # Create a list of strings: mutants
# mutants = ['charles xavier', 
#             'bobby drake', 
#             'kurt wagner', 
#             'max eisenhardt', 
#             'kitty pryde']

# # Create a list of tuples: mutant_list
# mutant_list = list(enumerate(mutants))

# # Print the list of tuples
# print(mutant_list)

# # Unpack and print the tuple pairs
# for index1, value1 in enumerate(mutants):
#     print(index1, value1)

# # Change the start index
# for index2, value2 in enumerate(mutants, 1):
#     print(index2, value2)

'''using zip'''

# # Create a list of tuples: mutant_data
# mutant_data = list(zip(mutants, aliases, powers))

# # Print the list of tuples
# print(mutant_data)

# # Create a zip object using the three lists: mutant_zip
# mutant_zip = zip(mutants, aliases, powers)

# # Print the zip object
# print(mutant_zip)

# # Unpack the zip object and print the tuple values
# for value1, value2, value3 in mutant_zip:
#     print(value1, value2, value3)

'''
result 
[('charles xavier', 'prof x', 'telepathy'), ('bobby drake', 'iceman', 'thermokinesis'), ('kurt wagner', 'nightcrawler', 'teleportation'), ('max eisenhardt', 'magneto', 'magnetokinesis'), ('kitty pryde', 'shadowcat', 'intangibility')]
    <zip object at 0x7f8981c748c0>
    charles xavier prof x telepathy
    bobby drake iceman thermokinesis
    kurt wagner nightcrawler teleportation
    max eisenhardt magneto magnetokinesis
    kitty pryde shadowcat intangibility
'''

'''---------------------------------------------------------------'''

'''unzip'''

# # Create a zip object from mutants and powers: z1
# z1 = zip(mutants, powers)

# # Print the tuples in z1 by unpacking with *
# print(*z1)

# # Re-create a zip object from mutants and powers: z1
# z1 = zip(mutants, powers)

# # 'Unzip' the tuples in z1 by unpacking with * and zip(): result1, result2
# result1, result2 = zip(*z1)

# # Check if unpacked tuples are equivalent to original tuples
# print(result1 == mutants)
# print(result2 == powers)


######################################################
######################################################
######################################################

'''processing large data '''


# Initialize an empty dictionary: counts_dict
counts_dict = {}

# Iterate over the file chunk by chunk
for chunk in pd.read_csv('tweets.csv', chunksize=10):

    # Iterate over the column in DataFrame
    for entry in chunk['lang']:
        if entry in counts_dict.keys():
            counts_dict[entry] += 1
        else:
            counts_dict[entry] = 1

# Print the populated dictionary
print(counts_dict)

'''processing large data '''

# Define count_entries()
def count_entries(csv_file, c_size, colname):
    """Return a dictionary with counts of
    occurrences as value for each key."""
    
    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Iterate over the file chunk by chunk
    for chunk in pd.read_csv(csv_file, chunksize=c_size):

        # Iterate over the column in DataFrame
        for entry in chunk[colname]:
            if entry in counts_dict.keys():
                counts_dict[entry] += 1
            else:
                counts_dict[entry] = 1

    # Return counts_dict
    return counts_dict

# Call count_entries(): result_counts
result_counts = count_entries('tweets.csv', 10, 'lang')

# Print result_counts
print(result_counts)

######################################################
######################################################
######################################################

'''Nested list expression'''

# # Create a 5 x 5 matrix using a list of lists: matrix
# matrix = [[col for col in range(5)] for row in range(5)]

# # Print the matrix
# for row in matrix:
#     print(row)

'''---------------------------------------------------------------'''

'''advanced list expression'''

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member for member in fellowship if len(member) > 6]

# Print the new list
print(new_fellowship)

'''advanced list expression 2'''

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create list comprehension: new_fellowship
new_fellowship = [member if len(member) >= 7 else "" for member in fellowship]

# Print the new list
print(new_fellowship)

'''advanced list expression with dictionary'''

# Create a list of strings: fellowship
fellowship = ['frodo', 'samwise', 'merry', 'aragorn', 'legolas', 'boromir', 'gimli']

# Create dict comprehension: new_fellowship
new_fellowship = {member: len(member) for member in fellowship}

# Print the new dictionary
print(new_fellowship)

# output:
#     {'frodo': 5, 'samwise': 7, 'merry': 5, 'aragorn': 7, 'legolas': 7, 'boromir': 7, 'gimli': 5}

######################################################
######################################################
######################################################

'''Generator'''

# # Create generator object: result
# result = (num for num in range(31))

# # Print the first 5 values
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))
# print(next(result))

# # Print the rest of the values
# for value in result:
#     print(value)


'''Generator 2'''
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(person) for person in lannister)


# Iterate over and print the values in lengths
for value in lengths:
    print(value)

# <script.py> output:
#     <generator object <genexpr> at 0x7fac475ef7b0>
#     6
#     5
#     5
#     6
#     7

'''Generator 3'''

lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

# Print the values generated by get_lengths()
for value in get_lengths(lannister):
    print(value)

# output :
# 6
# 5
# 5
# 6
# 7


######################################################
######################################################
######################################################

'''Final exercise : combination of all courses '''

# Define lists2dict()
def lists2dict(list1,list2):
    """Return a dictionary where list1 provides
    the keys and list2 provides the values."""

    # Zip lists: zipped_lists
    zipped_lists = zip(list1, list2)

    # Create a dictionary: rs_dict
    rs_dict = dict(zipped_lists)

    # Return the dictionary
    return rs_dict

# Call lists2dict: rs_fxn
rs_fxn = lists2dict(feature_names, row_vals)

# Print rs_fxn
print(rs_fxn)

'''-------------------------------------------------------------------'''

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])

# <script.py> output:
#     ['Arab World', 'ARB', 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'SP.ADO.TFRT', '1960', '133.56090740552298']
#     ['Arab World', 'ARB', 'Age dependency ratio (% of working-age population)', 'SP.POP.DPND', '1960', '87.7976011532547']
#     {'CountryName': 'Arab World', 'CountryCode': 'ARB', 'IndicatorName': 'Adolescent fertility rate (births per 1,000 women ages 15-19)', 'IndicatorCode': 'SP.ADO.TFRT', 'Year': '1960', 'Value': '133.56090740552298'}
#     {'CountryName': 'Arab World', 'CountryCode': 'ARB', 'IndicatorName': 'Age dependency ratio (% of working-age population)', 'IndicatorCode': 'SP.POP.DPND', 'Year': '1960', 'Value': '87.7976011532547'}


'''-------------------------------------------------------------------'''

# Import the pandas package
import pandas as pd

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names, sublist) for sublist in row_lists]

# Turn list of dicts into a DataFrame: df
df = pd.DataFrame(list_of_dicts)

# Print the head of the DataFrame
print (df.head())

'''-------------------------------------------------------------------'''


# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Skip the column names
    file.readline()

    # Initialize an empty dictionary: counts_dict
    counts_dict = {}

    # Process only the first 1000 rows
    for j in range(0, 1000):

        # Split the current line into a list: line
        line = file.readline().split(',')

        # Get the value for the first column: first_col
        first_col = line[0]

        # If the column value is in the dict, increment its value
        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1

        # Else, add to the dict and set value to 1
        else:
            counts_dict[first_col] = 1

# Print the resulting dictionary
print(counts_dict)

'''-------------------------------------------------------------------'''

# Define read_large_file()
def read_large_file(file_object):
    """A generator function to read a large file lazily."""

    # Loop indefinitely until the end of the file
    while True:

        # Read a line from the file: data
        data = file_object.readline()

        # Break if this is the end of the file
        if not data:
            break

        # Yield the line of data
        yield data
        
# Open a connection to the file
with open('world_dev_ind.csv') as file:

    # Create a generator object for the file: gen_file
    gen_file = read_large_file(file)

    # Print the first three lines of the file
    print(next(gen_file))
    print(next(gen_file))
    print(next(gen_file))

'''--------------------------------------------------------------------'''

'''Chunk large amount of data'''


# Import the pandas package
import pandas as pd

# Initialize reader object: df_reader
df_reader = pd.read_csv('ind_pop.csv', chunksize=10)

# Print two chunks
print(next(df_reader))
print(next(df_reader))

'''Chunk large amount of data 2'''

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Get the first DataFrame chunk: df_urb_pop
df_urb_pop = next(urb_pop_reader)

# Check out the head of the DataFrame
print(df_urb_pop.head())

# Check out specific country: df_pop_ceb
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

# Zip DataFrame columns of interest: pops
pops = zip(df_pop_ceb['Total Population'], df_pop_ceb['Urban population (% of total)'])

# Turn zip object into list: pops_list
pops_list = list(pops)

# Print pops_list
print(pops_list)

'''Chunk large amount of data 3'''

# Code from previous exercise
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)
df_urb_pop = next(urb_pop_reader)
df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']
pops = zip(df_pop_ceb['Total Population'], 
           df_pop_ceb['Urban population (% of total)'])
pops_list = list(pops)
print (pops_list)

# Use list comprehension to create new DataFrame column 'Total Urban Population'
df_pop_ceb['Total Urban Population'] = [int((x*y)/100) for (x, y) in pops_list]

# Plot urban population data
df_pop_ceb.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()

'''Chunk large amount of data 4'''

# Initialize reader object: urb_pop_reader
urb_pop_reader = pd.read_csv('ind_pop_data.csv', chunksize=1000)

# Initialize empty DataFrame: data
data = pd.DataFrame()

# Iterate over each DataFrame chunk
for df_urb_pop in urb_pop_reader:

    # Check out specific country: df_pop_ceb
    df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == 'CEB']

    # Zip DataFrame columns of interest: pops
    pops = zip(df_pop_ceb['Total Population'],
                df_pop_ceb['Urban population (% of total)'])

    # Turn zip object into list: pops_list
    pops_list = list(pops)

    # Use list comprehension to create new DataFrame column 'Total Urban Population'
    df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
    
    # Concatenate DataFrame chunk to the end of data: data
    data = pd.concat([data, df_pop_ceb])

# Plot urban population data
data.plot(kind='scatter', x='Year', y='Total Urban Population')
plt.show()


'''Chunk large amount of data final - creation of function to not reproduce the same thing'''


# Define plot_pop()
def plot_pop(filename, country_code):

    # Initialize reader object: urb_pop_reader
    urb_pop_reader = pd.read_csv(filename, chunksize=1000)

    # Initialize empty DataFrame: data
    data = pd.DataFrame()
    
    # Iterate over each DataFrame chunk
    for df_urb_pop in urb_pop_reader:
        # Check out specific country: df_pop_ceb
        df_pop_ceb = df_urb_pop[df_urb_pop['CountryCode'] == country_code]

        # Zip DataFrame columns of interest: pops
        pops = zip(df_pop_ceb['Total Population'],
                    df_pop_ceb['Urban population (% of total)'])

        # Turn zip object into list: pops_list
        pops_list = list(pops)

        # Use list comprehension to create new DataFrame column 'Total Urban Population'
        df_pop_ceb['Total Urban Population'] = [int(tup[0] * tup[1] * 0.01) for tup in pops_list]
        
        # Concatenate DataFrame chunk to the end of data: data
        data = pd.concat([data, df_pop_ceb])

    # Plot urban population data
    data.plot(kind='scatter', x='Year', y='Total Urban Population')
    plt.show()

# Set the filename: fn
fn = 'ind_pop_data.csv'

# Call plot_pop for country code 'CEB'
plot_pop(fn, 'CEB')

# Call plot_pop for country code 'ARB'
plot_pop(fn, 'ARB')


######################################################
######################################################
######################################################

'''CLASS'''

class Employee:
  
  # Include a set_name method
  def set_name(self, new_name):
    self.name = new_name

emp = Employee()

# Use set_name() on emp to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')
print(emp.name)

'''Class 2'''

class Employee:
  def set_name(self, new_name):
    self.name = new_name
  
  # Add set_salary() method  
  def set_salary(self, new_salary):
    self.salary = new_salary 

emp = Employee()

# Use set_name to set the name of emp to 'Korel Rossi'
emp.set_name('Korel Rossi')

# Set the salary of emp to 50000
emp.set_salary(50000)

# Print the emp object's salary
print(emp.salary)

'''Class 3'''

class Employee:
  def set_name(self, new_name):
    self.name = new_name

  def set_salary(self, new_salary):
    self.salary = new_salary 

  # Add a give_raise() method with amount as an argument
  def give_raise(self, amount):
    self.salary += amount

# Create the emp object
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary
print(emp.salary)

# Give emp a raise of 1500
emp.give_raise(1500)
print(emp.salary)


'''Class constructor'''

class Employee:
  def __init__(self, name, salary=0):
    self.name = name
    # Check if salary is positive
    if salary > 0:
      self.salary = salary
    else:
      self.salary = 0
      print("Invalid salary!")

  def give_raise(self, amount):
    self.salary += amount

  def monthly_salary(self):
    return self.salary / 12
      
emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)


'''Class constructor 2 '''

# Define and initialize the Calculator class
class Calculator:
  def __init__(self, num_one, num_two):
    self.num_one = num_one
    self.num_two = num_two
  
  # Create the addition method
  def addition(self):
    return self.num_one + self.num_two
  
  # Create the subtraction method
  def subtraction(self):
    return self.num_one - self.num_two
  
  # Create the multiplication method
  def multiplication(self):
    return self.num_one * self.num_two


'''Class attibutes 1 '''

class Player:
    MAX_POSITION = 10 # Global variable
    def __init__(self, position):
        if position <= Player.MAX_POSITION:
              self.position = position
        else:
              self.position = Player.MAX_POSITION

# Create Players p1 and p2
p1 = Player(9)
p2 = Player(5)

print("MAX_POSITION of p1 and p2 before assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

# Assign 7 to p1.MAX_POSITION
p1.MAX_POSITION = 7

print("MAX_POSITION of p1 and p2 after assignment:")
# Print p1.MAX_POSITION and p2.MAX_POSITION
print(p1.MAX_POSITION)
print(p2.MAX_POSITION)

# output :
# MAX_POSITION of p1 and p2 before assignment:
# 10
# 10
# MAX_POSITION of p1 and p2 after assignment:
# 7
# 10

'''Classmethod 1'''

# class Person:
#   CURRENT_YEAR = 2024
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
  
#   # Add a class method decorator
#   @classmethod
#   # Define the from_birth_year method
#   def from_birth_year(cls, name, birth_year):
#     # Create age
#     age = Person.CURRENT_YEAR - birth_year
#     # Return the name and age
#     return cls(name, age)

# bob = Person.from_birth_year("Bob", 1990)


'''Classmethod 2'''

class BetterDate:
#   def __init__(self, year, month, day):
#     self.year, self.month, self.day = year, month, day
    
#   # Define a class method from_str
#   @classmethod
#   def from_str(cls, datestr):
#     # Split the string at "-"
#     parts = datestr.split("-")
#     year, month, day = int(parts[0]), int(parts[1]), int(parts[2])
#     # Return the class instance
#     return cls(year, month, day)

# # Create the xmas object      
# xmas = BetterDate.from_str("2024-12-25")   
# print(xmas.year)
# print(xmas.month)
# print(xmas.day)


''' inheritance '''

# class Counter:
#     def __init__(self, count):
#        self.count = count

#     def add_counts(self, n):
#        self.count += n

# class Indexer(Counter):
#     pass

''' inheritance 2 '''

# class Employee:
#   def __init__(self, name, salary=30000):
#     self.name = name
#     self.salary = salary

#   def give_raise(self, amount):
#     self.salary += amount

# class Manager(Employee):
#   # Add a constructor 
#   def __init__(self, name, salary=50000, project=None):
    
#     # Call the parent's constructor   
#     Employee.__init__(self, name, salary)
    
#     # Assign project attribute
#     self.project = project

#   def display(self):
#     print("Manager ", self.name)


''' inheritance 3 '''

# class Employee:
#   def __init__(self, name, salary=30000):
#     self.name = name
#     self.salary = salary

#   def give_raise(self, amount):
#     self.salary += amount

# class Manager(Employee):
#   def display(self):
#     print("Manager ", self.name)

#   def __init__(self, name, salary=50000, project=None):
#     Employee.__init__(self, name, salary)
#     self.project = project

#   # Add a give_raise method
#   def give_raise(self, amount, bonus=1.05):
#     new_amount = amount * bonus
#     Employee.give_raise(self, new_amount)
    
# mngr = Manager("Ashta Dunbar", 78500)
# mngr.give_raise(2000, bonus=1.03)
# print(mngr.salary)


'''overloading equality'''

class BankAccount:
  # Modify to initialize a number attribute
  def __init__(self, number, balance=0):
    self.balance = balance
    self.number = number
      
  def withdraw(self, amount):
    self.balance -= amount 
    
  # Define __eq__ that returns True if the number attributes are equal 
  def __eq__(self, other):
    return other.number == self.number   

# Create accounts and compare them       
acct1 = BankAccount(123, 1000)
acct2 = BankAccount(123, 1000)
acct3 = BankAccount(456, 1000)
print(acct1 == acct2)
print(acct1 == acct3)

'''overloading equality 2'''

class BankAccount:
  def __init__(self, number, balance=0):
    self.number, self.balance = number, balance
      
  def withdraw(self, amount):
    self.balance -= amount 

  # Modify to add a check for the class type
  def __eq__(self, other):
    return (self.number == other.number) and (type(self) == type(other))

acct = BankAccount(873555333)
pn = Phone(873555333)

# Check if the two objects are equal
print(acct == pn)

# output : False
# In [1]: # pn == acct
# Out[1]: # True
# In [2]: # acct == pn
# Out[2]: # False

'''
Python always calls the child's __eq__() method when comparing a child object to a parent object.
'''

'''
using __repr__ to display, more suitable for developer (prefer that)
'''

class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
      
    # Add the __repr__() method  
    def __repr__(self):
        emp_str = f"Employee('{self.name}', {self.salary})"  
        return  emp_str

emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))


'''
using __str__ to display, more suitable for end user
'''
class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary
            
    # Add the __str__() method
    def __str__(self):
      emp_str = f"""Employee name: {self.name}
Employee salary: {self.salary}"""
      return emp_str

emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)

'''
Exception
'''

# Modify the function to catch exceptions
def invert_at_index(x, ind):
  try:
    return 1/x[ind]
  except ZeroDivisionError:
    print("Cannot divide by zero!")
  except IndexError:
    print("Index out of range!")
 
a_list = [5,6,0,7]

# Works okay
print(invert_at_index(a_list, 1))

# Potential ZeroDivisionError
print(invert_at_index(a_list, 2))

# Potential IndexError
print(invert_at_index(a_list, 5))

'''Custom exception '''
class SalaryError(ValueError): 
  pass
class BonusError(SalaryError): 
  pass

class Employee:
  MIN_SALARY = 30000
  MAX_BONUS = 5000

  def __init__(self, name, salary = 30000):
    self.name = name    
    if salary < Employee.MIN_SALARY:
      raise SalaryError("Salary is too low!")      
    self.salary = salary
    
  # Raise exceptions  
  def give_bonus(self, amount):
    if amount > Employee.MAX_BONUS:
      raise BonusError("The bonus amount is too high!")  
        
    elif self.salary + amount <  Employee.MIN_SALARY:
      raise SalaryError("The salary after bonus is too low!")
      
    self.salary += amount

'''
Notice that if you raise an exception inside an if statement, you don't need to add an else branch to run the rest of the code.
Because raise terminates the function, the code after raise will only be executed if an exception did not occur.
'''

######################################################
######################################################
######################################################

'''API request - urllib'''

from urllib.request import urlopen

with urlopen('http://localhost:3000/lyrics/') as response:
  
  # Use the correct function to read the response data from the response object
  data = response.read()
  encoding = response.headers.get_content_charset()

  # Decode the response data so you can print it as a string later
  string = data.decode(encoding)
  
  print(string)

'''API request - requests / it's the same but request is more easier / The requests package even took care of decoding the response for you'''

# Import the requests package
import requests

# Pass the API URL to the get function
response = requests.get('http://localhost:3000/lyrics')

# Print out the text attribute of the response object
print(response.text)


'''constructing url with a parms'''

# Create a dictionary variable with query params
query_params = {"artist":"Deep Purple"}

# Pass the dictionary to the get() function
response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

print(response.text)

'''constructing url with a parms 2 '''

# Add the `include_track` parameter
query_params = {'artist': 'Deep Purple', 'include_track' : True}

response = requests.get('http://localhost:3000/lyrics/random', params=query_params)

# Print the response URL
print(response.url)

# Print the lyric
print(response.text)

''' send a post request '''

# Create a dictionary with the playlist info
playlist_data = {"Name": "Rock Ballads"}

# Perform a POST request to the playlists API with your dictionary as data parameter
response = requests.post('http://localhost:3000/playlists', data=playlist_data)
print(response.text)

''' send a delete request '''

# Perform a DELETE request to the playlist API using the path to playlist with PlaylistId 2
requests.delete('http://localhost:3000/playlists/2')

# Get the list of all existing playlists again
response = requests.get('http://localhost:3000/playlists')
print(response.text)



'''Response code and API'''

response = requests.get('http://localhost:3000/lyrics')

# Check the response status code
if (response.status_code == 200):
  print('The server responded succesfully!')

  '''-------------------------------------------------------------------'''

'''Response code and API 2'''

response = requests.get('http://localhost:3000/movies')

# Check if the response.status_code is equal to the requests.codes value for "200 OK"
if (response.status_code == requests.codes.ok):
  print('The server responded succesfully!')
  
# Or if the request was not successful because the API did not exist
elif (response.status_code == requests.codes.not_found):
  print('Oops, that API could not be found!')


  '''-------------------------------------------------------------------'''

''' headers API with request'''

response = requests.get('http://localhost:3000/lyrics')

# Print the response content-type header
print(response.headers['content-type'])

'''-------------------------------------------------------------------'''

''' retrieve a lyric using the JSON format! '''

# Set the content type to application/json
headers = {'accept': 'application/json'}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Print the response's text
print(response.text)

'''-------------------------------------------------------------------'''

'''Handling content-types errors'''


# Add a header to use in the request
headers = {"accept":"application/xml"}
response = requests.get('http://localhost:3000/lyrics', headers=headers)

# Check if the server did not accept the request
if (response.status_code == 406):
  print('The server can not respond in XML')
  
  # Print the accepted content types
  print('These are the content types the server accepts: ' + response.headers['accept'])
else:
  print(response.text)

#   output : The server can not respond in XML
# These are the content types the server accepts: application/json, text/plain


'''------------------------------------------------------------------------------'''

''' Basic Authentication with requests '''

# Create the authentication tuple with the correct values for basic authentication
authentication = ("john@doe.com","Warp_ExtrapolationsForfeited2" )

# Use the correct function argument to pass the authentication tuple to the API
response = requests.get('http://localhost:3000/albums', auth=authentication)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')


'''------------------------------------------------------------------------------'''
''' API key authentication with requests - Post '''

# Create a headers dictionary containing and set the API key using the correct key and value 
headers = {"Authorization": "Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3"}
# Add the headers dictionary to the requests.get() call using the correct function argument
response = requests.get('http://localhost:3000/albums', headers=headers)

if(response.status_code == 200):
    print("Success!")
elif(response.status_code == 401):
    print('Authentication failed')
else:
    print('Another error occurred')


'''------------------------------------------------------------------------------'''
''' receiving json - API '''

headers = {
    'Authorization': 'Bearer ' + API_TOKEN,
    # Add a header to request JSON formatted data
    "accept": "application/json"
}
response = requests.get('http://localhost:3000/albums/1/', headers=headers)

# Get the JSON data as a Python object from the response object
album = response.json()

# Print the album title
print(album['Title'])

'''------------------------------------------------------------------------------'''
''' sending json - API '''

playlists = [{"Name":"Rock ballads"}, {"Name":"My favorite songs"}, {"Name":"Road Trip"}]

# POST the playlists array to the API using the json argument
requests.post('http://localhost:3000/playlists/', json=playlists)

# Get the list of all created playlists
response = requests.get('http://localhost:3000/playlists')

# Print the response text to inspect the JSON text
print(response.text)


'''------------------------------------------------------------------------------'''
''' Handling error for request - API '''

# Import the correct exception class
from requests.exceptions import HTTPError

url ="http://localhost:3000/albums/"
try: 
    r = requests.get(url) 
	# Enable raising errors for all error status_codes
    r.raise_for_status()
    print(r.status_code)
# Intercept the error 
except HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')



'''------------------------------------------------------------------------------'''
''' Respecting API rate limits '''

longestTrackLength = 0
longestTrackTitle = ""
headers = {'Authorization': 'Bearer 8apDFHaNJMxy8Kt818aa6b4a0ed0514b5d3'}
page_number = 1

while True:
    params = {'page': page_number, 'per_page': 500}
    response = requests.get('http://localhost:3000/tracks', params=params, headers=headers)
    response.raise_for_status()
    response_data = response.json()
    
    print(f'Fetching tracks page {page_number}')

    if len(response_data['results']) == 0:
        break

    for track in response_data['results']:
        if(track['Length'] > longestTrackLength):
            longestTrackLength = track['Length']
            longestTrackTitle = track['Name']

    page_number = page_number + 1
    
    # Add your fix here
    time.sleep(3)

print('The longest track in my music library is: ' + longestTrackTitle)





















