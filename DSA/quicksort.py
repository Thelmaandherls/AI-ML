import sys 
from load import load_numbers

if len(sys.argv) < 2:
    print("Usage: python -i bogo_sort.py <numbers_file_or_directory")
    sys.exit(1)
numbers = load_numbers(sys.argv[1])
print(numbers)

# futher dec the number of comaprisons made - faster than selection_sort 
# relies on recusion by calling itslef with incrmeentally smaller 
# subsets of the list that I want to sort 
def quicksort(values):
    # base case - if there are 0 / 1 element 
    if len(values) <=1:
        return values 
    
    # rely on divide and conquer approach aka take prob and keep 
    # splitting it until it's easy to solve aka splitting lsit into smaller 
    # lists but it's a complex process 
    # take the first val in the lsit and call it the pivot and assing to it's own var 
    # break the left over list into 2 sublsits - one for less and the other 
    # for greater than the pivot - these sublits are not sorted but if they were could just join 
    # sort the sublists by calling the quicsort algo recursively 
    # for first sublis,t take the first item as a picot again and then do the same thing
    # iteratively until each just a ingle elemnt and join, then do the same for the 
    # other greater than original pivot 
    # finished quicsort will put anhything less thnan or equal to in the finished quicksort 
    # all empty lsits are discarded
    less_than_pivot = []
    greater_than_pivot =[]
    pivot = values[0]
    for val in values[1:]:
        if val <= pivot:
            less_than_pivot.append(val)
        else:
            greater_than_pivot.append(val)
    # Calls not seen in the print statement are for calls to lists with 0/1 elements 
    print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

print(numbers)
sorted_numbers = quicksort(numbers)
print(sorted_numbers)