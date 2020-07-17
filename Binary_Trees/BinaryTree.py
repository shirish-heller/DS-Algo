class Node:
    def __init__(self, val, left, right):
        self.val=val
        self.left=left
        self.right=right
    
    def print(self):
        print("\n val="+str(self.val)+"--:::--left="+str(self.left)+"--:::--right="+str(self.right))

class BinaryTree:
    def __init__(self):
        self.root=None

    def createRootNode(self, val, left, right):
        self.root=Node(val, left, right)