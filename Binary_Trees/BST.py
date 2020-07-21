from BinaryTree import Node

class BST:
    def __init__(self, root):
        self.root=Node(root, None, None)
        self.left=None
        self.right=None
    
    def insertNode(self, node, newVal):
        if(node==None):
            return Node(newVal, None, None)
        if(node.val>newVal):
            node.left=self.insertNode(node.left, newVal)
        elif(node.val<newVal):
            node.right=self.insertNode(node.right, newVal)
        return node
    
    def deleteNode(self, node, valToDel):
        if(node==None):
            return False
        if(node.val>valToDel):
            node.left=self.deleteNode(node.left, valToDel)
            # return True
        elif(node.val<valToDel):
            node.right=self.deleteNode(node.right, valToDel)
            # return True
        else:
            if(node.left==None or node.right==None):
                if(node.left==None and node.right==None):
                    # Case where node to be deleted has no child
                    return None
                else:
                    # Case where node to be deleted has 1 child
                    temp=node.right if node.left==None else node.left
                    return temp
            else:
                # Case where node to be deleted has 2 childs
                successor=self.__getSuccessor(node.left)
                successor.left=node.left
                successor.right=node.right
                return successor
        
        return node

    def __getSuccessor(self, node):
        if(node.right==None):
            return node
        successor=self.__getSuccessor(node.right)
        if(node.right.val==successor.val):
            node.right=None
        return successor

#Iterative approach
    # def insertNode(self, val):
    #     node=self.root
    #     while(node!=None):
    #         if(val>node.val):
    #             if(node.right):
    #                 node=node.right
    #             else:
    #                 node.right=Node(val, None, None)
    #                 return
    #         else:
    #             if(node.left):
    #                 node=node.left
    #             else:
    #                 node.left=Node(val, None, None)
    #                 return

    def isPresent(self, val):
        node=self.root
        while(node!=None):
            if(val==node.val):
                return True
            elif(val>node.val):
                if(node.right):
                    node=node.right
                else:
                    node.right=Node(val, None, None)
                    return False
            else:
                if(node.left):
                    node=node.left
                else:
                    node.left=Node(val, None, None)
                    return False

bst=BST(4)
bst.insertNode(bst.root, 2)
bst.insertNode(bst.root, 6)
bst.insertNode(bst.root, 20)
bst.insertNode(bst.root, 22)
bst.insertNode(bst.root, 10)
bst.insertNode(bst.root, 15)
bst.insertNode(bst.root, 17)
bst.insertNode(bst.root, 1)
bst.insertNode(bst.root, 7)

bst.deleteNode(bst.root, 20)
a=bst.isPresent(20)


