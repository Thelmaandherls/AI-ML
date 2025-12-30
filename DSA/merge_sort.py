# will use an array / python list 
# simialr implementation conceptually to ll but will have to write more 
# code due to list traversal and how nodes are arranged 
def merge_sort(list):
    """ 
    Sort the given list in an ascending order 
    Create and return a new sorted list - other implementations 
    will sort the list we pass in in an operation known as sort 
    in palce but returning a new list makes it easier to understand
    the code but each of these have strategies have their own 
    implications
    Return a new sorted list 
    3 main steps in merge sort 
    divide: find the midpoint of the list and dividie evenly itno sublists 
    conquer: recursively sort the sublist that was created from previous step
    combine: merge the recusively sorted sublists into a single lsit from previous step
    """
    # recursive func has a basic pattern - a base case that includes a stopping condion 
    # some logic that breaks down the problem and recusively calls itself 
    # this stopping condition is the end goal - a sorted array thf need to come 
    # up w a stopping condition / base case which is simplest codnition that 
    # satisfies this end result 
    # 2 values that fit - a single element list or empty lsit - in these scenario have no work to do 
    # as is already sorted thf we call this naively sorted 
    
    if len(list) <=1:
        return list 
    
    # Div list into sublist 
    # split is a global func that we have to write 
    left_half, right_half = split(list)

    # conquer step - sort each sublist and return new sorted sublist 
    # recursive step that further splits sublist into 2 until reach a single 
    # element / empty list 
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    # combine step 
    return merge(left, right)

def split(list):
    """  
    Divide the unsorted list at midppoint into sublist 
    Return two sublists - left and right 
    """

    # Determine mid point of the lsit using floor division 
    mid = len(list) // 2

    # Extract portions of the list to return using list slicing 
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """  
    Merges two lists / arrays, sorting them in the process 
    Returns a new merged list 
    """

    # Need to sort the values in both list thf need to compare 
    # vals from each list by creating 2 local vars to keep track
    # of index vals for each list 

    l = []
    i = 0 # index in left list 
    j = 0 # inde in righ list

    # want to keep sorting the values until have iterated through 
    # both lists 
    while i < len(left) and j < len(right):
        # First comparison operation will be on the first element 
        # of eahc list respectively as i and j = 0
        # getting the first value out of both lists as now i and j = 0
        if left[i] < right[j]:
            # Val in left index is less than right index val then the val in 
            # left is less thna right thf placed at position 0 in new array ;
            l.append(left[i])
            # move forward to eval next item in left lsit 
            i += 1
        else:
            # if val at left[i] >= right[i] then put val of right[j]
            # at the start of the new lsit and moveforward one 
            l.append(right[j])
            j += 1

        # the left array could be larger than the right or vice versa - 
        # this can occur w an odd number array size than contains 3
        # elements for exmaple 
        # this while loop uses an and condition where the var used to 
        # store the index need to be less thna the length of the list 
        # thf is the left list is shorter than the right then the first 
        # condition returns false and the entire loop returns false thf 
        # the while loop terminates and all the vals in the right lsit
        #  will be moved to the new combined list thf need to account 
        # for this using 2 more while loops
        # 
        #  account for when the right lsit is shorter than the left and the 
        # previous loop terminated as we reached the end of the right loop first
        # will add the remaining elements in the left to the new lsits w/o
        # comapriing as assuming within the lsit, the elements are already sorted 
        # keep the loop goign until at last index and incrementing the index w
        # every iteration of the loop
        while i < len(left):
            l.append(left[i])
            i += 1

        # when left is shorter than right 
        while j < len(right):
            l.append(right[j])
            j += 1
        
        return l 
    
def verify_sorting(list):
    n = len(list)

    # Naively sorted 
    if n == 0 or n == 1:
        return True 
            
    # comapre the first to second value and then every value from then onwards
    return list[0] < list[1] and verify_sorting(list[1:])

# testing 
'''
test_lsit = [54, 12, 89,5, 90, 22, 56, 79, 10]
l = merge_sort(test_lsit)
print(l)
'''
        





    