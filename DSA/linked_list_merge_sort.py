from linked_list import LinkedList

# Testing it works 
''' l = LinkedList()
l.add(1)
print(l) '''

def merge_sort(linked_list):
    '''  
    Sorts a linked lsit in ascending order 
    - Recursively divide the ll sublsits contianing a single node 
    - Repeatedly merge sublsit to produce sorted sublsit until 1 remaisn 

    Return sorted ll 
    '''

    # Stopping condition base don naively sorted list - 1 element or empty
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    # split into left and right half by traversing the lsit 
    # using a helper method to make it easier 
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    '''  
    Divdie the sunorted lsit at midpoint into sub-linked-lsit
    With slit type, can rely on the fact of using an index and using 
    list slicing to split into 2 list would work ven if an empty lsit is parsed 
    But have no automatic behaviour like that thf need to account for that
    in ll
    '''
    # ll can be none if call split on a ll w 1 node thf left = 1 and half = none
    # assing the entire lsit to left half and none to the right 
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        # Could also assign the single element list or none 
        # to left and create new empty ll and assign to rh but 
        # it's unecessary work

        return left_half, right_half
    else:
        # Account for non-empty ll 
        # Calc the size of the list usign size methfo 
        size = linked_list.size()
        mid = size // 2

        # gte the node at that midpoint 
        # deduct 1 to get index value as size returns a val greater than max index val
        mid_node = linked_list.node_at_index(mid - 1)

        # split the lsit 
        # left half = entire ll
        left_half = linked_list
        # right half = new instance of ll which is empty
        right_half = LinkedList()
        # assing the rh the node that comes after the midpoint of the original ll 
        # as the head of the newly created right ll
        right_half.head = mid_node.next_node
        # Assign none to next node property on mid mode to srver the connection and 
        # me the midnode the tail node of left ll 
        mid_node.next_node = None

        return left_half, right_half
    
def merge(left, right):
    # like w split, after carrying out comaprison operation, also need to 
    # swap references to corrspsonding ndoes 
    '''  
    Merges two ll, sorting by data in the nodes 
    Returns a new merged list
    '''
    # Compare vals from two ll and then return a new ll w 
    # nodes where the data is sorted 
    # creatig a new ll that contians nodes from mergring left and right 
    merged = LinkedList()

    # Adding a fake head to this lsit thf when adding sroted node,s can dec 
    # the amount of code that we need to write by not worrying if we're at the 
    # head of the list. once done,assign the first sorted node as the 
    # head and discard the fake head 
    merged.add(0)

    # declare a var current to point to head of the lsit 
    current = merged.head

    # Get refernce to the head of each of the ll - left and right aka 
    # obtain head nodes for left and right ll 
    left_head = left.head 
    right_head = right.head

    # Iterate over left and right until we reach the tail node of either 
    # will keep runnign as long as one is true / has a node / value 
    while left_head or right_head:
        # Traverse the lsit w every iteration 
        # Once hit tail node of one lsit, any left over nodes in othe rlsit 
        # don't need a comaprison operation, just add to the merged lsit 

        # if head ll is none - past the tail of left thf add all the 
        # nodes from right ll to merged ll
        if left_head is None:
            # current points to head of merge lsit that will be returned
            current.next_node = right_head
            # move right head forward to next node
            # this terminates the node on the next iteration 
            # call next on right to set loop condition to False
            right_head = right_head.next_node

            # keep clling split until have lsits w just a single head, comapre the 
            # data and see which one is less, the smaller one is assigned as head 
            # oon the finalmerged lsit thf one half e.g. left is none on the next pass
            # through the loop then assign right head to next node making both 
            # lsits none and either one beig none will make while loop stop 
        # another way to do this is if the the head node of right = None, ast the tail 
        # thf add tail node from left to merged ll 
        elif right_head is None:
            current.next_node = left_head
            # Call next on left to set loop condition to False
            # now left head is None 
            left_head = left_head.next_node
        
        # when either right or left head is the tail node = have reached the bottom
        # of our split - hae single element ll or emoty ll

        # evlauting a node that is not at either tail nodes  thf need to campre the actual 
        # data values in each node 
        else:
            # Not at either tail node 
            # Obtain node data to perfrom comaprison operations 
            left_data = left_head.data
            right_data = right_head.data 

            # If data on left < right, set curent to left node 
            if left_data < right_data:
                current.next_node = left_head

                # Move left head to next node in the merge list as want lsit to 
                # be in asc order thf assign left node to be next node in merge lsit 
                # move left head forward to traverse down to the next node in that speciif clsit 
                left_head = left_head.next_node
            # if data on left > right, set current to right node 
            else:
                current.next_node = right_head
                # Move right head to next node 
                right_head = right_head.next_node
        # Move current to next node
        current = current.next_node
    # discard fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head 

    return merged 


l = LinkedList()
l.add(10)
l.add(43)
l.add(5)
l.add(98)
l.add(20)

print(l)
sorted_ll = merge_sort(l)
print(sorted_ll)