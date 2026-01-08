import sys 
from load import load_numbers

# slow but each pass brings us closer to completion 
# this implmentation will use 2 arrays: unsorted or sorted to keep the code simpler 
# sorted starts out empty but move values to it from the unsorted with each pass  to 
# the end of the sorted array therefore reinign compariosns will be 
# remianing vals in the usorted list 

numbers = load_numbers(sys.argv[1])

def selection_sort(values):
    sorted_list = []
    # Unsorted list print statement 
    print("%25s %25s" % (values, sorted_list))
    # loop once for each value in the list 
    for val in range(0, len(values)):
        index_to_move = index_of_min(values)
        # Call the opp method on the list and parse it the min index val
        sorted_list.append(values.pop(index_to_move))
        # Sorted lsit print statement 
        print("%25s %25s" % (values, sorted_list))
    return sorted_list

def index_of_min(values):
    """  
    For duplicates, it keeps the index and adds it onto the next pass so it doesn't 
    have to technically run again 
    """
    # Finds the min value in the list and returns it's index
    # marke the first val in the lsit as this which may not be the 
    # actual min but it's the smallest in this pass through the lsit 
    min_index = 0 
    # Loop through all values in the lsit after the first 
    for val in range(1, len(values)):
        if values[val] < values[min_index]:
            min_index = val 
    return min_index

print(selection_sort(numbers))

#unix code - need to be using a wsl terminal like ubuntu  
# cat file - prints th econtent of the file 
# adding time to any command arument prints how long it took to run the file 
# time has 3 ptputs - real, user and sys 
# real = how long it took to from start to beginnng but other 
# rogramms might tae cpu 
# user = how long the cpu too to run the code 
# sys = how long it too to run linux ernle calls 
# linux kernel = repsonsible for things lie networ communications and reading files 
# to eval code performance, tend to want to add user and sys results 

