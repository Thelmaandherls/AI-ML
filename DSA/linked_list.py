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
        Retirn num of nodes in a list and runs in linear time O(n)
        """
        # len on a python list = constant time 
        # len in linked list = linear time - have to go through each
        # itam until reach tail node 
        current = self.head
        count = 0

        # while current != None is the same as while current 
        while current:
            count += 1
            # thf when get to the tail and call next node, current will = 
            # None and the while loop terminantes 
            current = current.next_node

        return count 
    
    def add(self, data):
        """
        Adds new Node containing data at the head of the list - prepends
        Takes O(1) time
        """
        # Hold onto the data 
        new_node = Node(data)

        # Before setting new_node as head of the list, need to point the new_node
        # next prop at whatever node is currently at head so when set the new_node
        # as head, don't lose reference to head 
        new_node.next_node = self.head

        # insert operation is a reassignment of the node and next node props
        # thf this is a O(1) operation
        self.head = new_node

    def search(self, key):
        """ 
        Search for the first node containing data that matches the key
        Will return the first node that matches the key even if there are multiple 
        nodes that match 
        Returns 'None' if not found 
        Takes O(n) as have to check every data element 
        Strength of linked list comes from inserts and deletes so up to here it has no 
        strength against arrays 
        """
        current = self.head

        while current: 
            # return current if it matches the key
            if current.data == key:
                return current 
            else:
                # Assign cureent to the next node and check again if there's a key
                current = current.next_node
        return None # as we know we've hit the tail node
    
    def insert(self, data, index):
        """ 
        Inserts a new Node containign dat at index postion 
        Insertion takes O(1) time but finding the node at the insertion point 
        takes O(n) time (linear time) thf it takes an overall O(n)
        """
        # ll don't have index psotion but mimic it by counting the num of time 
        # we access next node. If the index = 0, then insert new node at head 
        # which is the same as adding add thf can call the add method 
        if index == 0:
            self.add(data)

        # Need to traverse the list to find the current node at that index 
        if index > 0: 
            # Create a new node that has data we wanrt to indert 
            new = Node(data)

            # everytime current.next_node is called, dec the val of psotion 
            # by 1and when psotion is 0, then have arrived at node that want 
            # to insert in/ In reality, don't want to dec postion all the way to 0
            # e.g. a ll w 5 nodes and want to insert at psotion 3 means that the 
            # nodes at psotion 2 and 3 need to be modded thf 2s next node attribute will 
            # point to the new node and the new node will point to psotion 3
            # insert = O(n) as don't need to shoft every element, just need to 
            # mod a few next_node references  
            # if dec psotion to 0, then end up with new node pointing to node 3, but no way
            # for it to point to node 2 as don't have node 2 rf thf easier to dec positions until 1 
            position = index 
            current = self.head 

            while position > 1:
                current = Node.next_node
                # when potion =1, loop exists and current will ref to the psotion 
                # before the insert point 
                position -= 1
            
            # Named the node before the new one previous 
            previous_node = current 

            # Named the node AFTER the new one next 
            next_node = current.next_node

            previous_node.next_node = new 
            new.next_node = next_node

    def remove(self, key):
        """ 
        Removes node containing data that matches the key and returns 
        the node or none if the key doesn't exist 
        tkes O(n) time 
        """
        # Remove method can be done in 2 ways: using a key 
        # which is the data the node stores thf to remove it, would first
        # need to search for data that matches the key 
        # the other is to do the remove at index method 
        # need to first search for data that matches the key 
        # need tomodify the next node references - the ndoe before the match
        # needs to point to the node after the match
        current = self.head
        previous_node = None 

        # Stopping consition until found is false aka key has not been found 
        found = False 

        # Keep iterating as long as current != None and found = false
        # found = false so not found = true. when find the key and found = true
        # not found = false then the while loop will stop
        while current and not found:
            # can run itno 3 situation:
                # 1. key matches the current node data nd the hea dis still at the 
                # top of the list as head doesn't have a prev node and is the only
                # node being handled by the list
            if current.data == key and current is self.head:
                found = True 
                # remove current node as as it's head node, do this by ref next node
                self.head = current.next_node
            # 2. key matches data in the node and it's a node that's not the head 
            elif current.data == key:
                # go to previous node and mod it's next_node ref to point to the node 
                # after the current node 
                found = True 
                previous_node.next_node = current.next_node
            # Current node doesn't contain data that matches the key
            # thf make prev point to current and current to net 
            else: 
                previous_node = current
                current = current.next_node
        # return the val being removed 
        return current 

# Strenght of ll comes in inserts and deletes in specific positions 
# Trty removing at index and node at index to allow to easily delete and read 
# vals at index 

    # Add a convenience method that will return a node at a given index 
    def node_at_index(self, index):
        # Instead of tarversing the slit inside of split fun in ll ms, can just 
        # call this and parse the midpoint index to perform the split 

        if index == 0:
            return self.head
        # Traverse the ll and conting up to the index as we citist each node
        else:
            current = self.head

            # Indciate out location in list
            position = 0

            # use a while loop to walk down the loop 
            while position < index:
                current = current.next_node
                position += 1 
                # Once psotion = index, current = node we're looking for 
                # thf can return it 
                return current 


    def __repr__(self):
        """ 
        Return a string representation of the list 
        Takes O(n) time  as everything to do w a ll reqs traversing
        """

        # python empty list 
        # going to add str that provide a desc of each node 
        nodes = [] 

        # pointer to head node 
        current = self.head 

        # While current is not none = not at the tail 
        while current:
            if current is self.head:
                # The data is extracted from current.data 
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else: 
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        
        # Join all the nodes and with every join, use the arrow
    
        return '-> '.join(nodes)

# cpmmands to run to lad the content 
# python -i linked_list.py
# -i = loads the content of the file into the terminal 

# checkc if the size func works
# l1 = LinkedList()
#N1 = Node(10)
#l.head = N1
#l.size()