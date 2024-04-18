tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    # print(data
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node0 = TreeNode(3)

node2.left = node3
node2.right = node5

node3.left = node1

node5.left = node3
node5.right = node7
node0.right = node4

node7.left = node6
node7.right = node8

print(node0.right.key)






