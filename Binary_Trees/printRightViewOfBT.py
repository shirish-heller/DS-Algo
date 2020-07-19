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
# tree.root.right.right.left.left=Node(20, None, None)

# printRightViewOfBT
# ************************************************************************************************************************
maxLevel=0
def printRightViewOfBT(node, level):
    global maxLevel
    if(node==None):
        return
    if(level>=maxLevel):
        print(node.val, end=" | ")
        maxLevel+=1
    printRightViewOfBT(node.right, level+1)
    printRightViewOfBT(node.left, level+1)
# ************************************************************************************************************************
print("\n RightViewOfBT is = ")
printRightViewOfBT(tree.root, 0)


