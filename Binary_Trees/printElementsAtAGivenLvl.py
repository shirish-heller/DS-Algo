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

# def printElementsAtAGivenLevel(node, level):
    # q=[node]
    # for currLevel in range(level+1):
    #     if(currLevel+1 == level):
    #         for parent in q:
    #             if(parent):
    #                 print(str(parent.left.val)) if parent.left else ""
    #                 print(str(parent.right.val)) if parent.right else ""
    #         return
    #     n=[]
    #     for node in q:
    #         if(node):
    #             n.append(node.left)
    #             n.append(node.right)
    #     q=n
# ************************************************************************************************************************

# printElementsAtAGivenLevel
# ************************************************************************************************************************

def printElementsAtAGivenLevel(node, level):
    if(level==1):
        print(node.val, end=" ")
    
    printElementsAtAGivenLevel(node.left, level-1) if node.left else None
    printElementsAtAGivenLevel(node.right, level-1) if node.right else None




print("printElementsAtAGivenLevel is = " )
printElementsAtAGivenLevel(tree.root, 4)

