# start at the top level for comparison.
result = equivalency_check(tree_a.node, tree_b.node):
    
if result is 0: # 0 means they are equivalent.
    # add the nodes of tree a's values to the total evaluation, and mark both tree's nodes as visited.
elif result is 1: # 1 means there is a type difference
    # If there is a type difference:
        # If the nodes are of atomic typing:
            # Add 1 to miss match & make both nodes visited.
        # Else If only one of the nodes is of type 'dict' or 'list'
            # Use the dict/list node to determine the amount of miss matches to add, and make both nodes visited.
        # Else: both nodes are of type dict/list
            # Use both nodes values to determine amount of mis matches, but subtract 1 for the intial node mismatch, and make them both visited.
    # Else: # Current nodes either have different values, or different child nodes. # RESULT IS 2
        # If current nodes are atomic:
            # add 1 to diff, mark both as visited & move on.
        # Else both are of type dict/list
            # Add 1 to matching
            # continue evaluating the children nodes (in a for/while loop?)
            # set as visited once all the chilren nodes have been marked as visited.
            
            
    # TODO: Each time we go back to the parent of a node, we check if all it's children are marked 'visited', to see if that node should be marked 'visited'.
            



for child in node.get_children():
    do_compare?