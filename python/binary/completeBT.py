# A binary tree node
class Node:

    # constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Given a binary tree, return true if the tree is complete, else return false
def isCompleteBT(root):

    # Base case: An empty tre is complete binary tree
    if root is None:
        return True

    # create an empty queue
    queue = []

    # create a flag variable which will be set true when a non-full none is seen
    flag = False

    # Do level order traversal using queue
    queue.append(root)
    while(len(queue) > 0):
        tempNode = queue.pop(0)  # dequeue

        # check if left child is present
        if (tempNode.left):

            # if we have seen a non-full node, and we see a node with non-empty left child,
            # then the given tree is not a complete binary tree
            if flag == True:
                return False

            # enqueue left child
            queue.append(tempNode.left)

            # if this is a full node, set the flag as true
        else:
            flag = True

        # check if the right child is present
        if (tempNode.right):
            # if we have seen a non-full node, and we see a node with non-empty right child
            # then the given tree is not a complete BT
            if flag == True:
                return False

            # Enqueue right child
            queue.append(tempNode.right)

        # if this is non-full node, set the flag as True
        else:
            flag = True

    # if we reach here, then the tree is complete BT
    return True


















