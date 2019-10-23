# This class will represent the tree datastructure necessary for processing and equating the data of json objects.

# Imports
from obj_node import node
    
class tree():
    
    def __init__(self, root):
        self.root_node = node(root)
        
        # Keeps track of the amount of given attribute types in each json object for comparison when they are being parsed
        atomic_values, list_count, dict_count, node_count = self.root_node.get_value_counts()
        # self.atomic_values = 0
        # self.list_count = 0
        # self.dict_count = 0
        
        print("Node count:", self.root_node.node_count)
        print("Atomic value count:", atomic_values)
        print("List count:", list_count)
        print("Dictionary Count:", dict_count)
        
        # TODO: Add functionality here for tree traversal
        # TODO: Consider adding comparison functionality here?