class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    string_list = ""
    current_node = self.get_head_node()
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
      current_node = current_node.get_next_node()
    return string_list
  
  def remove_node(self, value_to_remove):
    current_node = self.get_head_node()
    if current_node.get_value() == value_to_remove:
      self.head_node = current_node.get_next_node()
    else:
      while current_node:
        next_node = current_node.get_next_node()
        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node = None
        else:
          current_node = next_node

  def remove_every(self, value_to_remove):
    """This method removes every node that contains the value value_to_remove"""
    if self.get_head_node() == None:
      # Empty linked list; no work to do
      return
    # Remove all consecutive value_to_remove occurrences at the head
    while self.get_head_node().get_value() == value_to_remove:
      # Remove the next node
      self.head_node = self.head_node.next_node
      if self.head_node == None:
        # linked list is now empty
        return 
    # Remove all additional occurrences of value_to_remove
    current_node = self.head_node
    while current_node.next_node != None:
      if current_node.next_node.get_value() == value_to_remove:
        # Remove the next node
        current_node.next_node = current_node.next_node.next_node
      else:
        # Do not remove next node; simply advance to the next node
        current_node = current_node.next_node
    # reached end of linked list
    return