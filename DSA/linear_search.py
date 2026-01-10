# search through an unsorted lsit of items 

import sys 
from load_strings import load_strings

if len(sys.argv) < 2:
    print("Usage: python -i linear_search.py <file_name_or_folder>")
    sys.exit(1)

names = load_strings(sys.argv[1])

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

def index_of_items(list_being_searched, target):
    """  
    Start at the beginnign and comapre each tiem to target value one at a time 
    Also called sequential search 
    Loop through all names in the list and find the index of the name 
    as to where it appears on the list
    runtime - need to do one comaprision to the targetval for each item in the lsit
    thf O(n)
    """
    # loop form the first element to n-1
    # use rnage when looign through specific indexes
    for i in range(0, len(list_being_searched)):
        if target == list_being_searched[i]:
            return i
    # Item was not in the list 
    return None 

# calling the search func

for n in search_names:
    # using the values themseleves and not the index in the lsits 
    # parse the full lenght of names to search for and the name of the 
    # target and sorte it in a var then print the index 
    index = index_of_items(names, n)
    print(index)
