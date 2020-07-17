from BinaryTree import BinaryTree, Node

tree=BinaryTree()
tree.createRootNode(2, None, None)
tree.root.left=Node(7, None, None)
tree.root.left.left=Node(2, None, None)
tree.root.left.right=Node(6, None, None)
tree.root.left.right.left=Node(5, None, None)
tree.root.left.right.right=Node(11, None, None)

tree.root.right=Node(5, None, None)
tree.root.right.right=Node(9, None, None)
tree.root.right.right.left=Node(4, None, None)

# DifferenceOfEvenAndOddLevels
# ************************************************************************************************************************

def differenceOfEvenOddLevels(node):
    if(node==None):
        return 0
    return node.val-differenceOfEvenOddLevels(node.left)-differenceOfEvenOddLevels(node.right)

# ************************************************************************************************************************

print("Difference of Levels in BT is = " + str(differenceOfEvenOddLevels(tree.root)))