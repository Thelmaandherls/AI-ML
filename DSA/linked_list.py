class Node: 
    """
    An obj for storing a single node of a linked list. 
    Models two attributes: data and the link to the nect node in the lsit 
    """
    data = None # hold onto data that we're storing 
    next_node = None
    # N1.next_node = N2 means that n1 now points to N2

    # add constructor to make the node class to create 
    def __init__(self, data):
        self.data = data 

    # a str rep of what we want printed to the console when the obj 
    # inside of it is called inside of the console
    # %s = string interpolation aka a python way to subbing something into a string 
    # replaincing %s w self.data 
    def __repr__(self):
        return "<Node data: %s>" % self.data

# will def a head and this will model the only node the lsit 
# will have a ref to   
class LinkedList: 
    """
    Singly linked list
    """
    # head = None 
    # does the same things as the constructor fun below 

    def __init__(self):
        self.head = None 
        # models the only node the lsit will have ref to 
        # list traversal - finding a specific node by going from
        # one node to the next as every node points ot the next node
        # set the defualt val to None thf new lists are always empty 
        # self.head in the intialiser means that head is still created 

    # common op is checking if it contain any data or it's empty 
    # to check if a list is empty, would need to query the instance vars
    # head and so on everytime but we don't want to dieally show the inner
    # working of the ds to code that uses it  thf instead we make the op
    # more explicity by creating a method that checks to see if head is None
    
    def is_empty(self):
        return self.head == None
    
    # calc the size of the list - doens't ptovide any additonal fucntionality 
    # but makes exisitng funtionality easier to use 
    # could calc the len of linked list by traversing it every time using a loop
    # usntil we hit a tail node but it's a hassle every time 
    # this is a called a convenience method
    
    def size(self):
        """
        Retirn num of nodes in a list and runs in linear time 
        """
        # len on a python list = consnt time 
        # len in linked list = linear time - have to go through each
        # iteam until reach tail node 
        current = self.head
        count = 0

        # while current != None is the same as while current 
        while current:
            count += 1
            # thf when get to the tail and call next node, current will = 
            # None and the while loop terminantes 
            current = current.next_node

        return count 

    


