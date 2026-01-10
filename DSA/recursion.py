# The ability for a func to call on itself 
# like a chian reaction 

# a func to add all the nums in an array which = lsit in python
def add_numbers(numbers):
    total = 0 
    for num in numbers:
        total += num
    return total

# Recursion is not always the best approach and this approach uses
# python slicing syntax which is a way to get a series of vals from a list
# object[start:end:step]
# this func throws the error: RecursionError: maximum recursion depth exceeded
# as sum throws itself into an infinite loop and eep callign itslef 
# as when we get down to a lsit of just one lelement and take a slice from 
# just a one elemtn list and take a slice form the second element, it's an empty 
# list and it keeps being passed therefore need to add a abse case 
# a stopping condition to prevent an ongoing loop 
def recurisve_sum(numbers):
    # a base case = alternative to a recursive case - a condition where 
    # recursion should occur - for this func, it's when there are still elements 

    # if empty, return 0
    if not numbers:
        return 0
    # show the recurive call to sum aand what it's being called with 
    # therefore only the recurive call is shown first and not the first actual 
    # call to the func thf ignoring the firts item in the list 
    # as it's beign called recusively, it ignores the first item in each list
    # this keeps going until you have an empty list and at this point none of 
    # the recurisve call to sum has returned yet - eahc waiting on the recusive call it 
    # made to sum to complete - this triggers the base case 
    # python and oher progrmaming langauge use : call stack - to keep trac of series of func 
    # calls where each func call is added to the stack along with the place in the code that
    # it needs to return when it completes
    # the base case is tirggered, and the 0 value is added to it's caller. the caller 
    # adds the 0 to the first and only val in it's list which was rhe last value  taen off 
    # then it iteravely going bacwards 
    print("calling recurive_sum(%s)" % numbers[1:])
    remaining_sum = recurisve_sum(numbers[1:])
    # Show which of the calls the func is returnnign and what it's returning 
    print("calling to recurive_sum(%s) retuning %d + %d" % (numbers, numbers[0], remaining_sum))

    return numbers[0] + remaining_sum

print(add_numbers([1,2,4,5]))
print(recurisve_sum([1,2,4,5]))
# python repl = read evaluate print loop which is just typing python 
# into the command line 

# 2 fundamental of recursion 
''' 
needs a recusive case that causes it to call itself 
needs to eventually reach a bse case that causes the recursion to stop 
'''