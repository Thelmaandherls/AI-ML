import sys 
from load_strings import load_strings

if len(sys.argv) < 2:
    print("Usage: python -i linear_search.py <file_name_or_folder>")
    sys.exit(1)

names = load_strings(sys.argv[1])

# need to load unsorted names form a file, sort it and then load sorted names 
# into a new file 

# use quickksort to sort lsit of strings and just call it on the 
# lsit of names 

def quicksort(values):
    if len(values) < 1:
        return values
    
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

sorted_names = quicksort(names)

for n in sorted_names:
    print(n)


# to do a redirect in wsl terminal, add to the end
# > directory/filename.extension 
# if the filename doens't exist, it will be created 
# if the file exists, it will be overwritten without asking
# now have a list of sorted names which can be laoded into bs to find the 
# index. it works by halving the slit until it finds the target index and 
# it's faster because it discards half the non-matching elements everytime 

search_names = [
    "Liam Carter",
    "Sophia Nguyen",
    "Ethan Brooks",
    "Ava Mitchell",
    "Noah Ramirez",
    "Olivia Thompson",
    "James Wilson",
    "Isabella Moore",
    "Lucas Anderson",
    "Mia Taylor",
    "Benjamin Martinez",
    "Charlotte Lee",
    "Henry Johnson",
    "Amelia White",
    "Alexander Harris",
    "Emily Clark",
    "Daniel Lewis",
    "Harper Walker",
    "Matthew Hall",
    "Evelyn Allen",
    "Joseph Young",
    "Abigail King",
    "Samuel Wright",
    "Ella Scott",
    "David Green",
    "Scarlett Adams",
    "Andrew Baker",
    "Grace Nelson",
    "Christopher Hill",
    "Chloe Rivera",
    "Joshua Campbell",
    "Victoria Perez",
    "Ryan Roberts",
    "Aria Turner",
    "Nathan Phillips",
    "Lily Parker",
    "Jonathan Evans",
    "Zoey Edwards",
    "Christian Collins",
    "Penelope Stewart",
    "Aaron Sanchez",
    "Riley Morris",
    "Isaac Rogers",
    "Nora Reed",
    "Thomas Cook",
    "Hannah Morgan",
    "Charles Bell",
    "Layla Murphy",
    "Caleb Bailey",
    "Stella Cooper",
    "Anthony Richardson",
    "Paisley Cox",
    "Dylan Howard",
    "Audrey Ward",
    "Elijah Torres",
    "Brooklyn Peterson",
    "Jordan Gray",
    "Savannah Ramirez",
    "Adam James",
    "Camila Watson",
    "Ian Brooks",
    "Sarah Kelly",
    "Julian Price",
    "Autumn Bennett",
    "Kevin Wood",
    "Lucy Barnes",
    "Brandon Ross",
    "Madison Henderson",
    "Jason Coleman",
    "Naomi Jenkins",
    "Zachary Perry",
    "Aaliyah Powell",
    "Connor Long",
    "Elena Patterson",
    "Justin Hughes",
    "Ariana Flores",
    "Austin Washington",
    "Leah Butler",
    "Dominic Simmons",
    "Claire Foster",
    "Parker Gonzales",
    "Violet Bryant",
    "Miles Alexander",
    "Ruby Russell",
    "Cole Griffin",
    "Kinsley Diaz",
    "Tyler Hayes",
    "Maria Myers",
    "Owen Ford",
    "Willow Hamilton",
    "Xavier Graham",
    "Maya Sullivan",
    "Leo Wallace"
]

def binary_search(list_being_searched, target):
    first = 0 
    last = len(list_being_searched) -1

    # if first and last are equal, that means that the list is empty and 
    # there's no match but keep looping until them
    while first <= last:
        midpoint_index = (first + last) // 2
        # if midpoint f the lsit matches the target
        if list_being_searched[midpoint_index] == target:
            return midpoint_index
        # if midpoint in the lsit is less than target thf 
        # target val can't be at the midpoint or any index below that
        # so move the start of first range to the value after the midpoint 
        elif list_being_searched[midpoint_index] < target:
            first = midpoint_index + 1
        else:
            # if midpoint value is greater than the target 
            last = midpoint_index - 1
    # No match
    return None


for n in search_names:
    index = binary_search(names, n)
    print(index)