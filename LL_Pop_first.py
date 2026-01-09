"""def pop_first(self):
  if self.length==0:
    return None
    temp=self.head
    self.head=self.head.next
    temp.next=None
    self.length-=1 
    if self.length==0:
      self.tail=None
    return temp
    
my_linked_list=LinkedList(2)
my_linked_list.append(1)


my_linked_list.print_list()"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return temp

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next



my_linked_list = LinkedList(2)
my_linked_list.append(1)

my_linked_list.print_list()



my_linked_list.pop_first()
my_linked_list.print_list()


#Output is wrong 211 instead of 1 only come 

