# Exmaple of a bad algo
import random 
import sys 
from load import load_numbers 

#sys.argv gives us command line arguments to the script
# sys.argv[0] = script name
# sys.argv[1] = first argument after the script name - need to specify the directory 
# to look into in the command terminal or add a safety at the topf for errors

if len(sys.argv) < 2:
    print("Usage: python -i bogo_sort.py <numbers_file_or_directory")
    sys.exit(1)
numbers = load_numbers(sys.argv[1])
print(numbers)

# bogo_sort randomly rearranges the lsit continously thf need 
# a func to detect if the lsit is sorted returnign true or false 
def is_sorted(values):
    #  looping through all the numeric vals and then -1 to make it an index
    for index in range(len(values) - 1):
        # if the list is sorted, every value in it will be less than 
        # what comes after 
        # < - the list is form highest to lowest 
        # > - the lsit is from lowest to highest
        if values[index] > values[index + 1]:
            return False
    return True 

# func to do actual sorting 
def bogo_sort(values):
    # To chec how efficient it is - track num of attempts 
    attempts = 0
    while not is_sorted(values):
        # Looping until the is_sorted func returns true 
        # randomises the order of elements until the lsit returns true 
        # how many shuffles have already happened
        print(attempts)
        random.shuffle(values)
        # how many shuffles have been performed so far
        # print(attempts)
        attempts +=1
    return values

print(bogo_sort(numbers))

# Issue with bogo_sort = doesn't make any rpogress to sorting the list with each run 
# Stumbling on a solutin is just due to luck 