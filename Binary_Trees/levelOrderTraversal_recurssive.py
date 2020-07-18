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

# printElementsAtAGivenLevel
# ************************************************************************************************************************

def levelOrderTraversal_recurssive(node):
    q=[node]
    def bfs(node):
        if(node.left):
            q.insert(0, node.left)
        if(node.right):
            q.insert(0, node.right)
    
    while(len(q)!=0):
        print(q[-1].val)
        bfs(q.pop())
        

# ************************************************************************************************************************

print("LOT of the given tree is: ")
levelOrderTraversal_recurssive(tree.root)