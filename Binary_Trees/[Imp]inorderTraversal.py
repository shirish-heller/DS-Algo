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

# ************************************************************************************************************************
def inorder(node):
    if(node==None):
        return
    inorder(node.left)
    print(str(node.val))
    inorder(node.right)
# ************************************************************************************************************************

print("\n********* IN-ORDER-TRAVERSAL *********\n")
inorder(tree.root)
print("\n******************\n")




