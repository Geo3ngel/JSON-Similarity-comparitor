# TODO: Compare similarity of the two objects.

# Imports
from obj_tree import tree

class Equivalence_Processor():
    
    def __init__(self):
        # sim = matched values (atomic & lists/dicts)
        self.sim = 0
        # diff_val = atomic values that are different and have a valid node to compare against in the other tree.
        self.diff_val = 0
        
        # diff_no_other_a = have no valid node to compare against in the other tree.
        # diff_no_other_b = have no valid node to compare against in the other tree.
        self.diff_no_other_a = 0
        self.diff_no_other_b = 0
        
        self.tree_a = None
        self.tree_b = None
        
        # total = sim + diff_val + 
    # TODO: Change to just take in Comparison object?
    def compare_json_objs(self, comparison):
        
        # Direct equivalence check
        if comparison.json_object_a != comparison.json_object_b:
            # Calculate how similar they are, if at all. 
            print("NEQ")
            self.compare_objects(comparison)
            return 0
            
        else: 
            print("EQ")
            # The JSON objects are 100% equivalent 
            return 1
    # Check if their base structure is at all similar

    # Go into those structures for further analysis.
    # - Do a deep dive for both to get an idea of their entire structure, as if branching out a tree, then compare tree structures.
    # Referenced: https://pdfs.semanticscholar.org/e0ae/7666afa22d4fc1a955efc71f8c46f0ee791b.pdf for comparison of Tree data structures.

    # Evaluates all the properties of the passed in object and returns them as a list
    def expand_object(self, obj):
        pass

    # Takes in a Comparison object and goes through it's json objects
    def compare_objects(self, comparison):
        obj_a = comparison.json_object_a
        obj_b = comparison.json_object_b
        
        # lists for keeping track of the current object value's states for comparison
        self.tree_a = tree(obj_a)
        self.tree_b = tree(obj_b)
        
        # IF the nodes are equal between both trees at the defined point:
        # - Take the node_count of either node and add it to the shared total, then mark those nodes, as well as their children, as visited. 
        # - It would also be valid to simply mark that node as visited and go back.
        # ELSE IF a node differs/is not equal between the trees, we first check if there is a type difference. 
        # - If there is, we count the total nodes that are dependant on that node, and return them to the total for not matched
        # - Also add those that do not match to a diff set for that node.
        # ELSE there is a not a type difference between the nodes
        # - go deeper & do not classify this node as being different.
        
        self.traverse_trees()

        # Split stats print:
        atomic_values_a, list_count_a, dict_count_a, node_count_a = self.tree_a.get_values()
        atomic_values_b, list_count_b, dict_count_b, node_count_b = self.tree_b.get_values()
        
        print("Node count: A;", node_count_a, "B;", node_count_b)
        print("Atomic value count: A;", atomic_values_a, "B;", atomic_values_b)
        print("List count: A;", list_count_a, "B;", list_count_b)
        print("Dictionary Count: A;", dict_count_a, "B;",dict_count_b)
        
        total = self.sim + self.diff_val
        print("Similar:", self.sim)
        print("Total:", total)
        print("Percent Similarity:", self.sim/total)
        
            
    def traverse_trees(self):
        
        # We are done traversing the trees when the root nodes are both visited.
        while (not self.tree_a.root_visited()) and (not self.tree_b.root_visited()):
            
            if self.node_comparison(self.tree_a.get_next_node(), self.tree_b.get_next_node()):
                # If true, we need to go a layer deeper. So we go inside the current set of nodes, and evaluate their children.
                # Choose the first child that has not been visited.
                
                print("TREE A CHILDREN:", len(self.tree_a.get_next_node().get_children()))
                for child in self.tree_a.get_next_node().get_children():
                    print(child.get_node_type())
                # TODO: NOTICE: Possible problem here due to the children lists being out of order??? If thats the case, I need to sort them!
                print("TREE B CHILDREN:", len(self.tree_b.get_next_node().get_children()))
                for child in self.tree_b.get_next_node().get_children():
                    print(child.get_node_type())
                    
                for child in self.tree_a.get_next_node().get_children():
                    if not child.is_visited():
                        self.tree_a.set_next_node(child)
                        break
                        
                for child in self.tree_b.get_next_node().get_children():
                    if not child.is_visited():
                        self.tree_b.set_next_node(child)
                        break
            
            else:
                # If false, it has evaluated somehow. So we set the next node to the current node's parent.
                if (self.tree_a.get_next_node().get_parent() is not None) and (self.tree_b.get_next_node().get_parent() is not None):
                    self.tree_a.set_next_as_parent()
                    self.tree_b.set_next_as_parent()

                # After updating the next node, we check if it should be set to visited (if all it's children are visited)
                visit_check_a = True
                for child in self.tree_a.get_next_node().get_children():
                    if not child.is_visited():
                        visit_check_a = False
                        break
                        
                visit_check_b = True
                for child in self.tree_b.get_next_node().get_children():
                    if not child.is_visited():
                        visit_check_b = False
                        break
                    
                # If one node is set to visited, the other node should also be set to visited, and if it has any remaining children, they should be accounted for by adding their values to diff_val.
                if (not visit_check_a) and (not visit_check_b):
                    # Don't set either to visited.
                    pass
                elif visit_check_a and visit_check_b:
                    # Both are visited fully
                    self.tree_b.get_next_node().set_visited()
                    self.tree_a.get_next_node().set_visited()
                else:
                    # Only one was finished being visited, which means we use the remaining children of the other node for their values and set it to visited anyway.
                    if visit_check_a:
                        for child in self.tree_b.get_next_node().get_children():
                            if not child.is_visited():
                                self.diff_val += child.get_total()
                    else:
                        for child in self.tree_a.get_next_node().get_children():
                            if not child.is_visited():
                                self.diff_val += child.get_total()
                                
                    self.tree_b.get_next_node().set_visited()
                    self.tree_a.get_next_node().set_visited()
                    
                    
                    
    # Adds the node's compared value to the totals, and returns whether or not the nodes need to be explored deeper.
    def node_comparison(self, node_a, node_b):
        # Checks if the nodes are equivalent
        if node_a is node_b:
            print("NODES ARE EQ")
            # Adds the nodes of tree a to similarity value
            self.sim += node_a.get_total()
            
            # Mark both nodes as visited.
            node_a.set_visited()
            node_b.set_visited()
            return False
        
        # Checks if the nodes have a type difference
        elif node_a.get_node_type() is not node_b.get_node_type():
            print("TYPE DIFF")
            # Checks if the nodes are both of atomic typing
            if node_a.type_check() == -1 and node_b.type_check() == -1:
                self.diff_val += 1
            elif node_a.type_check() == -1 or node_b.type_check() == -1:
                # Use the dict/list node to determine the amount of miss matches to add
                if node_a.type_check() == -1:
                    self.diff_val += node_b.get_total()
                else: 
                    self.diff_val += node_a.get_total()
            else:   # Both nodes are of type dict/list
                # Use both nodes values to determine amount of mis matches, but subtract 1 for the intial node mismatch
                self.diff_val += node_a.get_total() + node_b.get_total() - 1
            
            # Set both nodes as visited, as we won't need to explore them deeper.
            node_a.set_visited()
            node_b.set_visited()
            return False
        
        # Checks if the nodes values are different but they are of the same type.
        else:
            print("SAME TYPE")
            # Checks if the nodes are atomic, meaning they just have different values.
            if node_a.type_check() == -1 and node_b.type_check() == -1:
                # Add 1 to diff, mark both as visited.
                self.diff_val += 1
                node_a.set_visited()
                node_b.set_visited()
            else: # Both are of either type 'DICT' or 'LIST'
                # Add 1 to similarity, as these nodes technically match, the only difference is the children nodes.
                self.sim += 1

                if len(node_a.get_children()) > 0 and len(node_b.get_children()) > 0:
                    # Signal to go deeper into these nodes
                    return True
                elif len(node_a.get_children()) > 0:
                    # Node b is an empty dict/list, so we add the value of node a minus 1 to the total diff value.
                    self.diff_val += node_a.get_total()-1
                    node_a.set_visited()
                    node_b.set_visited()
                else:
                    # Node a is an empty dict/list, so we add the value of node a minus 1 to the total diff value.
                    self.diff_val += node_b.get_total()-1
                    node_a.set_visited()
                    node_b.set_visited()
                    
                return False