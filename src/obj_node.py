# This class will represent each node in the object tree

# Constants:
OTHER = -1
LIST = 0
DICT = 1

class node():
    
    total_depth = 0
    
    def __init__(self, variable):
        self.var = variable
        self.visited = False
        # Sets up the children nodes
        self.children = []
    
        type_val = self.type_check()
        if type_val is LIST:
            self.process_list()
        elif type_val is DICT:
            self.process_dict()
        else:
            # TODO: Evaluate this properly via comparison
            print("TYPE:", type(self.var), "Evaluate Me:", self.var)
            
        self.depth = len(self.children)
        # TODO: Verify this number
        node.total_depth += self.depth
        
    def has_next(self):
        pass

    # Function to tell if we can split the current var deeper, or should just evaluate it at it's current depth
    def type_check(self):
        if (type(self.var) is list):
            return LIST
        elif(type(self.var) is dict):
            return DICT
        else:
            return OTHER
        
    # Processes lists into nodes for tree traversal
    def process_list(self):
        for var in self.var:
            self.children.append(node(var))
            print("VAR:", var)
            
    # Processes dictionaries into nodes for tree traversal
    def process_dict(self):
        for key in self.var.keys():
            # TODO: Consider storing variable name too? (key)
            # Or possibly come up with a dictionary comparison function.
            # Evaluate keys, then go deeper if needed for comparison.
            self.children.append(node(self.var.get(key)))
