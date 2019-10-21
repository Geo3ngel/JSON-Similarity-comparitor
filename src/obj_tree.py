# This class will represent the tree datastructure necessary for processing and equating the data of json objects.

# Imports
from obj_node import node
class tree():
    
    def __init__(self, root):
        self.root_node = node(root)
        print(node.total_depth)