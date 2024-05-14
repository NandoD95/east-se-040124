# Sequence Types
# docs: 
# https://docs.python.org/3/tutorial/datastructures.html
import ipdb

#lists, tuples, dictionaries, and sets are all individual data types that are used to store collections of data.  they each have their own unique properties/behaviors.  a lot of those behaviors overlap

# Creating Lists
#✅ 1. Create a list of 10 pet names
pets = ['Apollo', 'Bailey', 'Daisy', 'Kami', 'Bachman', 'Bruno', 'Mya', 'Tobi']

#------------------------ Reading Information from Lists
#✅ 1a. Return the first pet name 
pets[0]

#✅ 1b. Return the last value
pets[7]
pets[len(pets)-1]
pets[-1]

#✅ 1c. Return all pet names beginning from the 3rd index
pets[3:]

#✅ 1d. Return all pet names before the 3rd index
pets[:3]

#✅ 1e. Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th
pets[3:7]

#✅ 1f. Find the index of a given element
pets.index('Kami')

#✅ 1g. Reverse the original list
# mutate our list, destructive
# does not return anything
pets.reverse()


#✅ 1h. Return the frequency of a given element 
pets.count('Kami')

#---------------------------------- Updating Lists
#✅ 1i. Change the first element to all uppercase
pets[0] = pets[0].upper()

#---------------------------------- Adding items to list
#✅ 1j. Append a new name to the list
pets.append('Deja')

#✅ 1k. Add a new name at a specific index
pets.insert(3, 'Bebesita')

#✅ 1l. Add two lists together 
new_pet_names = ['Lilo', 'Avery']
combined_lists = new_pet_names + pets

#---------------------------------- Removing 
#✅ 1m. Removes and returns the final element from the list
 pets.pop()

#✅ 1n. Remove element by specific index
pets.pop(2)

#✅ 1o. Remove a the first instance of a specific element 
pets.remove('Deja')

#✅ 1p. Remove all pet names from the list
pets.clear()

#---------------------------------- Tuple 
# can't mutate tuples
# can have repeats
#🛑 Using a trailing comma for a singleton tuple: a, or (a,)
#✅ 2. Create a Tuple of pet 10 ages 
ages = (1, 10, 5, 3, 5, 8, 2, 0)


#✅ 2a. Print the first pet age
print(ages[0])

#---------------------------------- Testing Changeability 
#✅ 2b. Attempt to remove an element with .pop (should error)
# AttributeError:

#✅ 2c. Attempt to change the first element (should error)
# TypeError:

#---------------------------------- Tuple Methods
#✅ 2d. Return the frequency of a given element
ages.count(5)

#✅ 2e. Return the index of first matching element 
ages.index(0)

#---------------------------------- Demo Sets
#✅ 3. Create a set of 3 pet foods
# cannot be duplicate 
# pop() method removes random 
pet_foods = {'Blue Buffalo', 'Royal Canine', 'Costco'}

# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 4. Create a dictionary of pet information with the keys name, age and breed
# KEYS AS STRINGS
pet = {
    'name': 'Rose';
    'age': 11;
    'breed': 'Frenchie'
}

#✅ 4a.  Use dict to create a dictionary of pet information with the keys name, age and breed
dict(name='Rose', age='11', breed='Frenchie')
#---------------------------------- Reading
#✅ 4b. Print the pet attribute of name using bracket notation
print(pet['name'])

#✅ 4c. Print the pet attribute of age using .get
print(pet.get('age'))

#---------------------------------- Updating 
#✅ 4d. Update the pets age to 12
pet['age'] = 12

#✅ 4e. Update the other pets age to 26
pet.update(age=12)

#---------------------------------- Deleting
#✅ 4f. Delete a pets age using the del keyword 
del pet['age']

#✅ 4g. Delete the other pets age using the .pop, returns removed value
other_cat.pop('age')

#✅ 4h. Delete the last item in the pet dictionary using popitem()

other_cat.popitem() #only removes the last key value pair that was added 

#✅ 5. loop through a range of 10 and print every number within the range
for num in range(10):
    print(num)

#✅ 5a. loop through a range between 50 and 60 that iterates by 2 and print every number
#range(start, stop, increment)
for num in range(50,60, 2):
    print(num)

#✅ 5b. Loop through the pet_info list and print every dictionary  
pet_info = [
    {
        'name': 'Rose',
        'age': '10',
        'breed': 'dog'
    },    
    {
        'name': 'Kami',
        'age': '3',
        'breed': 'dog'
    },
    {
        'name': 'Bebesita',
        'age': '2',
        'breed': 'dog'
    },
]

for pet in pet_info:
    print(pet['name'])
    print(pet['age'])

#✅ 6. Create a function that takes a list as an argument. 

def print_list(lst):
    print(lst)

print_list(pet_info)
#✅ 7. Create a function that takes a list as an argument.(simple example) 



#✅ 8. Create a function that updates the age of a given pet
#replace_age(pet_info, "spot", 2) # => { 'name': "spot", 'age': 2, 'breed': "boxer"}
#replace_age(pet_info, "does_not_exist", 5) # => 'pet not found'
def replace_age (pet_list, name, new_age):
    found = Falso
    for pet in pet_list:
        if pet ['name'] == name:
            found = True
            pet['age'] = new_age
            break
    
    if not found:
        print('Pet Not Found!')

replace_age(pet_info, 'Kami', 4)

# map like 
#✅ 9. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase
pet_names = [pet['name' for pet in pet_info]]

# find like
#✅ 9a. Use list comprehension to find a pet named spot
[pet for pet in pet_info if pet['name'] == 'Spot']

# filter like
#✅ 9b. Use list comprehension to find all of the pets under 3 years old
older_pets = [pet for pet in pet_info if pet['age'] > 3]
young_pet = [pet for pet in pet_info if pet['age'] < 3]


ipdb.set_trace()