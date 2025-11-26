class LinkedList:
    def __init__(self,value):
        #create a new node
    def append(self,value):
        #create a new node
        #add a node
    def prepend(self,value):
        #create new Node
    def insert(self,index,value):
        #Create new Node
        #insert Node"""

class Node:
    def __init__(self,value):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

my_linked_list=LinkedList(4)
print(my_linked_list)
print(my_linked_list.head.value)
