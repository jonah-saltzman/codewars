# You are given a node that is the beginning of a linked list. This list always contains a tail and a loop.

# Your objective is to determine the length of the loop.

def loop_size(node):
    # seen is list of dictionaries containing node ID and position in the list
    seen = []
    
    # addresses is a list of all node IDs that have been seen
    addresses = []
    
    # counter indicating current position in linked list
    count = 1
    
    while True:
        # element to be added to list of dicts if ID hasn't been seen
        element = {'addr':id(node), 'pos':count}
        
        # if node hasn't been seen before, add element to "seen" and ID to "addresses", increment "count"
        if id(node) not in addresses:
            seen.append(element)
            addresses.append(id(node))
            count += 1
            node = node.next
            
        # once loop is identified, search elements in "seen" to find first node in loop, set loop_start to position of that node
        else:
            for n in seen:
                if n['addr'] == id(node):
                    loop_start = n['pos']
            break
            
    # size of loop equals position of last node seen minus position of first node in loop
    return count - loop_start
