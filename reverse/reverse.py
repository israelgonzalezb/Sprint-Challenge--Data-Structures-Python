class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
    # We'll start at the head of the list, checking if one exists... this is called "pivot"
    # We then check to see if the next node of the head exists
    # Does the next node's next node exist? if so...
    # We then set pivot's next node to be next node's next node
    # and move the next node to the head of the list
    # if next node's next node doesn't exist, then we set pivot's next to None and the list is reversed

    if self.head:
      pivot = self.head
      current = self.head.get_next()
      if current:
        pivot_next = current.get_next()
      else:
        pivot_next = None

    
      while current:
        
        self.add_to_head(current.get_value())
    
        pivot.set_next(pivot_next)
        current = pivot_next
        if current:
          pivot_next = current.get_next()
        else:
          pivot_next = None
      else:
        pivot.set_next(None)

    pass