# This class will represent each node in the object tree

import obj_tree

# Constants:
OTHER = -1
LIST = 0
DICT = 1

class node():
    
    total_depth = 0
    
    def __init__(self, variable, parent):
        # Gives this node a parent to reference for tree traversal
        self.parent = parent
        self.var = variable
        self.visited = False
        # bool value to represent if a node has been evaluated for it's similarity score.
        # This is to prevent parent nodes from contributing to similarity scores more than once.
        self.evaluated = False
        
        # Stores the type of this node for later comparison
        self.node_type = type(variable)
        
        # Sets up the children nodes
        self.children = []
        
        # Initializes the counter variables for each structure possible for json object
        self.atomic_values = 0
        self.list_count = 0
        self.dict_count = 0
        
        self.generate_children()
    
    # Generates the children nodes & tracks relevant values for comparison
    def generate_children(self):    
        type_val = self.type_check()
        
        if type_val is LIST:
            self.process_list()
            # Keep track of values for this!
            self.list_count += 1
        elif type_val is DICT:
            self.process_dict()
            self.dict_count += 1
        else:
            self.atomic_values += 1
            
        # Determines the amount of nodes in the current tree (starting from this node)
        self.node_count = 1
        for child in self.children:
            self.node_count += child.node_count
            self.atomic_values += child.atomic_values
            self.list_count += child.list_count
            self.dict_count += child.dict_count

    # Function to tell if we can split the current var deeper, or should just evaluate it at it's current depth
    def type_check(self):
        if (self.node_type is list):
            return LIST
        elif(self.node_type is dict):
            return DICT
        else:
            return OTHER
        
    # Processes lists into nodes for tree traversal
    def process_list(self):
        for var in self.var:
            self.children.append(node(var, self))
            
    # Processes dictionaries into nodes for tree traversal
    def process_dict(self):
        #print("DICT:", self.var)
        for key in self.var.keys():
            # TODO: Consider storing variable name too? (key)
            # Evaluate keys, then go deeper if needed for comparison.
            self.children.append(node(self.var.get(key), self))

    # Getters
    def get_parent(self):
        return self.parent

    def is_evaluated(self):
        return self.evaluated
    
    def get_children(self):
        return self.children

    def get_var(self):
        return self.var
    
    def get_value_counts(self):
        return self.atomic_values, self.list_count, self.dict_count, self.node_count
    
    def get_total(self):
        return self.node_count

    def get_node_type(self):
        return self.node_type

    def is_visited(self):
        return self.visited
    
    # Setters
    def set_visited(self):
        self.visited = True
        
    def set_evaluated(self):
        self.evaluated = True