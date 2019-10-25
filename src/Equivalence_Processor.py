# TODO: Compare similarity of the two objects.

# Imports
from obj_tree import tree

# TODO: Change to just take in Comparison object?
def compare_json_objs(comparison):
    
    # Direct equivalence check
    if comparison.json_object_a != comparison.json_object_b:
        # Calculate how similar they are, if at all. 
        print("NEQ")
        compare_objects(comparison)
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
def expand_object(obj):
    pass

# Takes in a Comparison object and goes through it's json objects
def compare_objects(comparison):
    obj_a = comparison.json_object_a
    obj_b = comparison.json_object_b
    
    # lists for keeping track of the current object value's states for comparison
    tree_a = tree(obj_a)
    tree_b = tree(obj_b)
    
    # IF the nodes are equal between both trees at the defined point:
    # - Take the node_count of either node and add it to the shared total, then mark those nodes, as well as their children, as visited. 
    # - It would also be valid to simply mark that node as visited and go back.
    # ELSE IF a node differs/is not equal between the trees, we first check if there is a type difference. 
    # - If there is, we count the total nodes that are dependant on that node, and return them to the total for not matched
    # - Also add those that do not match to a diff set for that node.
    # ELSE there is a not a type difference between the nodes
    # - go deeper & do not classify this node as being different.

    # Split stats print:
    atomic_values_a, list_count_a, dict_count_a, node_count_a = tree_a.get_values()
    atomic_values_b, list_count_b, dict_count_b, node_count_b = tree_b.get_values()
    
    print("Node count: A;", node_count_a, "B;", node_count_b)
    print("Atomic value count: A;", atomic_values_a, "B;", atomic_values_b)
    print("List count: A;", list_count_a, "B;", list_count_b)
    print("Dictionary Count: A;", dict_count_a, "B;",dict_count_b)
    
    # sim = matched values (atomic & lists/dicts)
    # diff_val = atomic values that are different and have a valid node to compare against in the other tree.
    
    # diff_no_other_a = have no valid node to compare against in the other tree.
    # diff_no_other_b = have no valid node to compare against in the other tree.
    
    # total = sim + diff_val + 
    
    # There will be a problem for ones of differing size, how do I compare the percentage difference this way?
    # Possibly see the total size of both, check the percentage matched for that one and report it that way? Or average?
    
    # TOTAL final matched count:
    
    
    # TOTAL diff count:
    
    # TODO: differentialte between structural difference & value difference?
    # Degree of similarity = sim/total
    # total = sim + diff_cal + diff_type_a + diff_type_b