class Node:
  def __init__(self, value):
    self.value = value  
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def insert_at_end(self, value):
    new_node = Node(value)
    if not self.head:
      self.head = new_node
    else:
      current = self.head
      while current.next:
        current = current.next
      current.next = new_node

  def display(self):
    current = self.head
    while current:
      print(current.value, end=" ")
      current = current.next

# Creating a linked list
my_list = LinkedList()
my_list.insert_at_end(5)
my_list.insert_at_end(10)
my_list.insert_at_end(15)
my_list.display()
print()
