import sys 
from load import load_numbers

if len(sys.argv) < 2:
    print("Usage: python -i mergesort.py <number_file_or_directory")
    sys.exit(1)

numbers = load_numbers(sys.argv[1])
# splits the lsits in halves recursively and themn sortes the halves and 
# eventually mcombines / merges them together 

# this is a recurve ms 
def merge_sort(values):
    """  
    No pivot to pick and lsit of number is always div in half, log n times 
    thf always has a big o runtime of O(n log n)
    whereas quicsort has a best case run time of O(n log n) and worst case of O(n2)
    yet it's used more often in mergesort in the real word 
    big o runtime only says the num of times an operation is performed 
    but doesn't describe how long it taes 
    ms takes longer than qs 
    big o = useful to quickly describe how the run time of an algo inc as the data 
    its operating on gets really big
    """
    if len(values) <= 1: 
        return values
    
    # need to know the index to split on by div len of list by 2 
    # floor division thf vals are rounded down if vals are 0.5 or less
    middle_index = len(values) // 2 
     
    left_half = merge_sort(values[:middle_index])
    right_half = merge_sort(values[middle_index:])

    print("%15s %-15s" % (left_half, right_half))
    sorted_values = []

    # merging the sorted lsits together and sorting as it's done 
    # will be moving from left to the right in the left half and 
    # right to left in the right half, copying vals to the sprted_vals
    # list as we traverse the list 
    # use the left and right index val to keep track of position 
    left_index = 0 
    right_index = 0

    # keep looping until all vals in left and right half are processed 
    while left_index < len(left_half) and right_index < len(right_half):
        # copy over the current vals first by testing if the vals on the left 
        # is less than the vals on the right 
        if left_half[left_index] < right_half[right_index]:
            sorted_values.append(left_half[left_index])
            left_index += 1 
        else:
            sorted_values.append(right_half[right_index])
            right_index += 1
    # one of the two unsorted halves still has a val remaining and the other 
    # is empty - won't waste time checing which is which, just copy 
    # the remainder of both into the sorted list
    sorted_values += left_half[left_index:]
    sorted_values += right_half[:right_index]

    return sorted_values

print(numbers)
sorted_numbers = merge_sort(numbers)
print(sorted_numbers)

