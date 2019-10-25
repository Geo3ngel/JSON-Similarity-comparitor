# This class will represent the tree datastructure necessary for processing and equating the data of json objects.

# Imports
from obj_node import node
    
class tree():
    
    def __init__(self, root):
        # initializes all the nodes in the tree.
        self.root_node = node(root, None)
        
        # Initializes the next node as the root
        self.next_node = self.root_node
        
    def get_next_node(self):
        return self.next_node
    
    def set_next_node(self, next_node):
        self.next_node =  next_node
    
    def set_parent_node(self):
        self.next_node.get_parent()
    
    def get_values(self):
        return self.root_node.get_value_counts()
        