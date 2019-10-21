# TODO: Compare similarity of the two objects.

def compare_json_objs(a, b):
    
    # Direct equivalence check
    if a == b:
        print("EQ")
        # The JSON objects are 100% equivalent 
        return 1
    else: 
        # Calculate how similar they are, if at all. 
        print("NEQ")
        return 0
# Check if their base structure is at all similar

# Go into those structures for further analysis.
# - Do a deep dive for both to get an idea of their entire structure, as if branching out a tree, then compare tree structures.
# Referenced: https://pdfs.semanticscholar.org/e0ae/7666afa22d4fc1a955efc71f8c46f0ee791b.pdf for comparison of Tree data structures.
