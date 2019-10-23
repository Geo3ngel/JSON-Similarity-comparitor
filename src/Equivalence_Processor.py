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
        
    # TODO: Evaluate similarity between these lists.
    # - Determine the similarity of each variable in the list
    # - If equal, get it's depth & return that value with (true)
    # - Else If not equal, go deeper into that object to find the diff. (Mark each similarity until then though)
    
    # DATA STRUCTURE FOR THIS: A tree with the ability to mark nodes as having been visited?
    

# Takes in two objects and exlpores their depths.
def recurse(json_object_a, json_object_b):
    # a and b are both dictionaries
    for p in json_object_a:
        print(p)
    print()
    for p in json_object_b:
        print(type(p))
        
    print(json_object_a.keys())
    for key in json_object_a.keys():
        print("Key", key, "=>", json_object_a.get(key))
        print(type(json_object_a.get(key)))
        if type(json_object_a.get(key)) is list:
            for dictionary in json_object_a.get(key):
                print("DICT:", dictionary)
                print("DICT TYPE:", type(dictionary))
        else:
            print("Not a dict")