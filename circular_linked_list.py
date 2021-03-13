#Josh Follmer

#this is a class for the things that are getting stored in the list
class Node:
    def __init__(self, data):
        #the variable for the content of the item
        self.data = data
        #this will be the connection to the next node. it is purposefully left undefined so it can be assinged later, but it needs to exist first
        self.next = None

    

#this is a class for the head node, or the one that will start the list
class CircularLinkedList:
    def __init__(self, node = None):
       #this is for the data that will be stored in the head
       self.head = node 
       if node:
           node.next = self.head

    def is_empty(self):
        return self.head == None


    def append_left(self, item):
        '''Puts a new item at the start of the list, making it the new head'''
        #makes a new node
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            new_node.next = self.head
            self.head = new_node
            temp.next = self.head


    def append_right(self, item):
        '''Adds an item to the end'''
        new_node = Node(item)
        #this is so it doesnt throw an error for the first append
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
        #starts at the head
            last = self.head
            #traverses the list. each time a next node exists, move on to the next and set the variable to it
            while(last.next != self.head):
                last=last.next
            last.next = new_node
            new_node.next = self.head
        
        

    def pop_left(self):
        '''Deletes the head, the second in the list becomes the new head'''
        #saves the current head as a temp variable
        old_head = self.head
        #the second node now becomes the head
        self.head = old_head.next
        #deletes the old head
        old_head = None


    #this is based from https://www.geeksforgeeks.org/remove-last-node-of-the-linked-list/#:~:text=Approach%3A%20To%20delete%20the%20last,pointer%20of%20that%20node%20null.&text=Create%20an%20extra%20space%20secondLast,till%20the%20second%20last%20node.&text=delete%20the%20last%20node%2C%20i.e.,second%20last%20node%20delete(secondLast.
    def pop_right(self):
        #this one is pretty redunant but i should be in the habit of making these
        '''deletes the last element in the list '''
        #makes a variable that will end up as the second last in the list
        second_last = self.head
        #while a node has two nodes in front of it, loops though the list
        while(second_last.next.next != self.head):
            second_last = second_last.next
        #removes the connection from the second last to the last
        second_last.next = None
        second_last.next = self.head
        
           
    def print_list(self):
        '''Prints the list'''
        if self.is_empty():
            return
        else:
        #sets a temp variable
            temp = self.head
            #while the current node exists
            while temp.next != self.head:
                #prints the data
                print(temp.data)
                #changes to the next node
                temp = temp.next
            print(temp.data)
        
    def get_len(self):
        '''Returns the lenth of the list'''
        #same thing as print_list, but adds one to the length each loop and returns the result
        temp = self.head
        length = 0
        while(temp.next != self.head):
            length += 1
            temp = temp.next
        return length

    def contains(self, key):
        '''Checks if the list contains the passed item'''
        temp = self.head
        while(temp.next != self.head):
            if temp.data == key:
                return True
            else: 
                temp = temp.next
        return False

    def has_cycle(self):
        #if the list has only one node, it cannot be a cycle
        if self.get_len() <= 1:
            return False
        #tortoise starts at the head of the list
        tortoise = self.head
        #hare starts at the second node
        hare = self.head.next
        
        while True:
            try:
                #each loops, tortoise advances to each node
                tortoise = tortoise.next
                #each loop, hare advances two nodes ahead
                hare = hare.next.next
            except:
                #if an exception occurs, which would happen if hare reaches a null value, it is not a cycle so return false
                return False

            if tortoise == hare:
                #if the tortoise and hare are at the same node, which could only happen if hare looped and caught up to tortoise, it is a cycle so return true
                if self.is_circle() == True:
                    print('Is a circle')
                return True

    def is_circle(self):
        #the pointer starts at the second node
        pointer = self.head
        try:
            #loops through as many times as the list is long 
            for i in range(self.get_len()):
                #each loops moves the pointer over one node
                pointer = pointer.next
        except:
            #if it ends as a null, it is not a cycle so return false
            print("Is not a cycle")
            return False
        #if the pointer ends at the head, return true
        if pointer == self.head:
            return True
        #else return false
        else:
            return False