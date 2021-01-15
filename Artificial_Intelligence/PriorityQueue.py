import math
class PriorityQueue:
    def __init__(self):
        self.queue = []
    
    def addNode(self, node):
        path = node[0]
        cost = node[1]
        self.queue.append(node)
        if(len(self.queue)!=0):
            self.__heapifyBottomTop__(len(self.queue)-1)
    def pop(self):
        self.swapNodes(0, len(self.queue)-1)
        minValue = self.queue.pop()
        self.__heapifyTopToBottom__()
        return minValue
    
    def isEmpty(self):
        return len(self.queue)==0

    def __heapifyTopToBottom__(self, index=0):
        leftChildIndex = self.getLeftChildIndex(index)
        rightChildIndex = self.getRightChildIndex(index)
        smallerNodeIndex = None
        if(leftChildIndex==None and rightChildIndex == None): return
        if(leftChildIndex and rightChildIndex):
            if(self.queue[leftChildIndex][1]<self.queue[rightChildIndex][1]):
                smallerNodeIndex = leftChildIndex
            else: smallerNodeIndex = rightChildIndex
        else:
            smallerNodeIndex = (leftChildIndex) if leftChildIndex!=None else rightChildIndex
        
        if(self.queue[index][1]>self.queue[smallerNodeIndex][1]): 
            self.swapNodes(index, smallerNodeIndex)
            self.__heapifyTopToBottom__(smallerNodeIndex)
        else: return
    
    def getLeftChildIndex(self, index):
        leftChildIndex = index*2+1
        if(leftChildIndex<len(self.queue)): return leftChildIndex
        else: return None

    def getRightChildIndex(self, index):
        rightChildIndex = index*2+2
        if(rightChildIndex<len(self.queue)): return rightChildIndex
        else: return None
        
    def __heapifyBottomTop__(self, index):
        parentIndex = self.getParentIndex(index)
        if(parentIndex!=None and self.queue[parentIndex][1]>self.queue[index][1]):
            self.swapNodes(index, parentIndex)
            self.__heapifyBottomTop__(parentIndex)
        else: return
        
    def swapNodes(self, index1, index2):
        [self.queue[index1], self.queue[index2]] = [self.queue[index2], self.queue[index1]]

    def getParentIndex(self, index):
        parentIndex = (math.ceil(index/2))-1
        if(parentIndex>=0 and parentIndex<len(self.queue)): return parentIndex
        else: return None
    
    def hasParentNode(self, index):
        parentIndex = self.getParent(index)
        return (parentIndex>=0 and parentIndex<len(self.queue))

# q = PriorityQueue()
# q.addNode(('AB', 70))
# q.addNode(('AD',60))
# q.addNode(('ABC',40))
# q.addNode(('ADF',45))
# q.addNode(('ABCE',50))
# q.addNode(('ABCQ',39))
# q.addNode(('ABCER',16))
# q.addNode(('ABCERT',10))
# q.addNode(('ABCQR',80))
# print(q.pop(), "\n")

# print(q.queue)