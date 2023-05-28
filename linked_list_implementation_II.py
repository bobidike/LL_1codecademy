# We'll be using our Node class
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

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# inserts nodes at beginning of LL
  def insert_beginning(self, new_value): 
    #instantiates a node with new_value
    new_node = Node(new_value)
    #links new_node to exisitng head_node
    new_node.set_next_node(self.head_node)
    #replaces current head_node with new_node
    self.head_node = new_node

# gives a string rep of our ll
  def stringify_list(self): 
    #going to collect all node values in linked list
    string_list =""
    #traverses the ll
    current_node = self.get_head_node() # acts like a TRAVERSER 

    while current_node != None:
      string_list+=str(current_node.get_value())+"\n" #get value from node and add2string
      current_node= current_node.get_next_node() # moves 2 next node
    return string_list
  
  #removes nodes 
  def remove_node(self,value_to_remove):
    #case head is node to be deleted
    current_node=self.head_node 
    # see if current node is not end of ll and is value we want deleted
    if current_node.get_value() == value_to_remove and current_node:
        #sets curr to next node in the list
        self.head_node= current_node.get_next_node()
        # get rid of element 
        current_node=None 
        return
    #case not head is node to be deleted, we use  a next node and current node to traverse
    else:
      # as long as element we are on is not null and is not what we are getting rid off 
      #we traverse the ll
      while current_node and current_node.get_value()!= value_to_remove:
        
        next_node = current_node.get_next_node() # next_node doesnt exist outside while loop

        if next_node.get_value() == value_to_remove:
          current_node.set_next_node(next_node.get_next_node())
          current_node =None
          return  
        current_node =next_node


        


  


# Test your code by uncommenting the statements below - did your list print to the terminal?
ll = LinkedList(5)
ll.insert_beginning(70)
ll.insert_beginning(5675)
ll.insert_beginning(90)
ll.remove_node(5)
print(ll.stringify_list())
