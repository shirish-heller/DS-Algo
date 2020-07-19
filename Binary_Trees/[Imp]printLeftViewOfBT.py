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

maxLevel=0
print("here is the variable"+ str(maxLevel))
# printLeftViewOfBT
# ************************************************************************************************************************
def printLeftViewOfBT(node, level):
    global maxLevel
    if(node==None):
        return
    if(level>=maxLevel):
        maxLevel=maxLevel+1
        print(node.val, end=" | ")

    printLeftViewOfBT(node.left, level+1)
    printLeftViewOfBT(node.right, level+1)

# ************************************************************************************************************************
print("printLeftViewOfBT of the given tree is: ")
printLeftViewOfBT(tree.root, 0)