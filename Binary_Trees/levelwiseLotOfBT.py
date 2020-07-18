from BinaryTree import BinaryTree, Node
from getHeightOfBT import getHeightOfBT
from printElementsAtAGivenLvl import printElementsAtAGivenLevel

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

# levelwiseLotOfBT
# ************************************************************************************************************************

def levelwiseLotOfBT(node):
    treeHeight=getHeightOfBT(node)
    for level in range(1,treeHeight+2):
        print("\n Level "+str(level)+":-")
        printElementsAtAGivenLevel(node, level) 

# ************************************************************************************************************************

print("Levelwise LOT of the given tree is: ")
levelwiseLotOfBT(tree.root)