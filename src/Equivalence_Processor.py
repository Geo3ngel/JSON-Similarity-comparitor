# TODO: Compare similarity of the two objects.

# Initial check: Are they completely equivalent?
def compare_json_objs(a, b):
    if a == b:
        print("EQ")
    else: 
        print("NEQ")
    

# Check if their base structure is at all similar

# Go into those structures for further analysis.
# - Do a deep dive for both to get an idea of their entire structure, as if branching out a tree, then compare tree structures.
# Referenced: https://pdfs.semanticscholar.org/e0ae/7666afa22d4fc1a955efc71f8c46f0ee791b.pdf for comparison of Tree data structures.
