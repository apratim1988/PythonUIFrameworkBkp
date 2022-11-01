#A linked list is a data structure made of a chain of node objects.
# Each node contains a value and a pointer to the next node in the chain.
class Node:
  # constructor
  def __init__(self, data, next=None):
    self.data = data
    self.next = next
# A Linked List class with a single head node
class LinkedList:
  def __init__(self):
    self.head = None
# Linked List with a single node
LL = LinkedList()
LL.head = Node(3)
print(LL.head.data)

# Creating a single node
first = Node(3)
print(first.data)

#Collections in python
# Counters
# OrderedDict
# DefaultDict
# ChainMap
# NamedTuple
# DeQue
# UserDict
# UserList
# UserString