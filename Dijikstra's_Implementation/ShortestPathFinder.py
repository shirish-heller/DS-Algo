class Node:
    def __init__(self, key, val):
        self.key=key
        self.value=val
        self.left=None
        self.right=None

class PriorityQueue:
    def __init__(self):
        self.heap=[]

    def addNode(self, key, val):
        newNode=Node(key,val)
        self.heap.append(newNode)
        if(len(self.heap)>1): self.__heapifyBottomToTop__(len(self.heap)-1)

    def isEmpty(self):
        return (True if len(self.heap)==0 else False)

    def __heapifyBottomToTop__(self, index):
        hasParent = self.hasParent(index)
        if(hasParent==False):
            return
        else:
            parentIndex = self.getParent(index)
            if(self.heap[parentIndex].value>self.heap[index].value):
                self.__swap__(parentIndex, index)
                self.__heapifyBottomToTop__(parentIndex)

    def hasLeftChild(self, i):
        if(self.getLeftChild(i)> len(self.heap)-1):
            return False
        else: return True
    
    def hasRightChild(self, i):
        if(self.getRigthtChild(i)> len(self.heap)-1):
            return False
        else: return True

    def hasParent(self, i):
        if(self.getParent(i) < 0):
            return False
        else: return True

    def __heapifyTopToBottom__(self, index):
        hasLeftChild=self.hasLeftChild(index)
        hasRightChild=self.hasRightChild(index)
        leftChildIndex=self.getLeftChild(index)
        rightChildIndex=self.getRigthtChild(index)
        if(hasLeftChild==False and hasRightChild==False):
            # Case where node has no children
            return
        elif(hasLeftChild==False):
            # Case where only right child Node is preset
            if(self.heap[index].value < self.heap[rightChildIndex].value):
                return
            else:
                self.__swap__(rightChildIndex, index)
                self.__heapifyTopToBottom__(rightChildIndex)
        
        elif(hasRightChild==False):
            # Case where only left child Node is preset
            if(self.heap[index].value < self.heap[leftChildIndex].value):
                return
            else:
                self.__swap__(leftChildIndex, index)
                self.__heapifyTopToBottom__(leftChildIndex)
        else:
            # Case where both the child nodes are present
            if(self.heap[leftChildIndex].value > self.heap[rightChildIndex].value):
                if(self.heap[index].value > self.heap[rightChildIndex].value):
                    self.__swap__(index, rightChildIndex)
                    self.__heapifyTopToBottom__(rightChildIndex)
            else:
                if(self.heap[index].value > self.heap[leftChildIndex].value):
                    self.__swap__(index, leftChildIndex)
                    self.__heapifyTopToBottom__(leftChildIndex)

    def __swap__(self, index1, index2):
        [self.heap[index1], self.heap[index2]] = [self.heap[index2], self.heap[index1]]

    def getParent(self, i):
        return ((i+1)//2)-1

    def getLeftChild(self, i):
        return ((i+1)*2)-1

    def getRigthtChild(self, i):
        return ((i+1)*2+1)-1

    def peekMinElement(self):
        return self.heap[0]
        
    def printHeap(self):
        for elm in self.heap:
            print(elm.key, ": ", elm.value, "\n")
    
    def getMinElement(self):
        minElement = Node(self.heap[0].key, self.heap[0].value)
        if(len(self.heap)>1):
            self.heap[0] = self.heap.pop()
            self.__heapifyTopToBottom__(0)
        else:
            self.heap.pop()
        return minElement

class Graph:
    def __init__(self, startingNode, endingNode):
        self.graph={}
        self.startingNode=startingNode;
        self.endingNode=endingNode;
    def __init__(self):
        self.graph={}
    def setStartingNode(self, node):
        self.startingNode=node;
    def setEndingNode(self, node):
        self.endingNode=node;
    def getNodes(self):
        return self.graph.keys()
    def checkIfNodePresent(self, node):
        return (False if(self.graph.get(node)==None) else True)
    def getEdgesForANode(self, node):
        return self.graph.get(node)
    def addNode(self, node):
        self.graph.update(node)
    def addEdge(self, fromNode, toNode, weight):
        self.graph.get(fromNode).update({toNode: weight})
        self.graph.get(toNode).update({fromNode: weight})
    def printGraph(self):
        print(self.graph)
    
def initialize():
    routeMap = Graph();
    inputFile = open("inputPS11.txt", "r")
    data = inputFile.read()
    print(data)
    rows = data.split("\n")
    for row in rows:
        if(row.find("Hospital") != -1):
            routeMap.setStartingNode(row.split(":")[1].strip())
        elif(row.find("Airport") != -1):
            routeMap.setEndingNode(row.split(":")[1].strip())
        else:
            route=row.split("/")
            startingNode=route[0]
            endingNode=route[1]
            weight=route[2]
            if(routeMap.checkIfNodePresent(startingNode)==False):
                routeMap.addNode({startingNode: {}})
            if(routeMap.checkIfNodePresent(endingNode)==False):
                routeMap.addNode({endingNode: {}})
            routeMap.addEdge(startingNode, endingNode, weight)
    
    routeMap.printGraph()
    return routeMap

def getShortestPath(routeMap):
    # Dijikstra's shortest path finding algo
    priorityQueue=PriorityQueue()
    nodeCosts={
        routeMap.startingNode: {
            "cost": 0, 
            "path": ""
        }
        }
    def calculateRouteCosts(node):
        edges=routeMap.graph.get(node)
        for items in edges.items():
            if(items[0]==routeMap.startingNode):
                continue
            if(nodeCosts.get(items[0])==None):
                priorityQueue.addNode(items[0], nodeCosts.get(node).get("cost")+int(items[1]))
            # updating node Costs
            if(nodeCosts.get(items[0]) and nodeCosts.get(items[0]).get("cost")!=None and nodeCosts.get(items[0]).get("cost") < (nodeCosts.get(node).get("cost")+int(items[1])) ):
                continue
            else:
                nodeCosts[items[0]]={
                    "cost": nodeCosts.get(node).get("cost")+int(items[1]),
                    "path": nodeCosts.get(node).get("path") + str(node) + ", "
                }
        if(priorityQueue.isEmpty()):
            return
        else: 
            calculateRouteCosts(priorityQueue.getMinElement().key)
        if(len(nodeCosts.keys())==len(routeMap.graph.keys())):
            return
    calculateRouteCosts(routeMap.startingNode)
    # print("routCosts = ", routeCosts)
    print("\n nodeCosts = \n", nodeCosts)
    # print(" \n\n Shortest path from starting node ", routeMap.startingNode, " to ending Node ", routeMap.endingNode, " is = ", nodeCosts.get(routeMap.endingNode).get("path") + routeMap.endingNode, " DISTANCE = ", nodeCosts.get(routeMap.endingNode).get("cost"))
    return nodeCosts;


def main():
    routeMap=initialize()
    routeCosts = getShortestPath(routeMap)
    averageSpeed=80
    timeTaken = (routeCosts.get(routeMap.endingNode).get("cost")/averageSpeed)*60
    formattedTimeTaken = str(timeTaken).replace(".", ":")

    output=open("outputPS11.txt", "w")
    output.write("Shortest route from the hospital '" + routeMap.startingNode + "' to reach the airport '" + routeMap.endingNode +  "' is ["+routeCosts.get(routeMap.endingNode).get("path")+routeMap.endingNode+"]")
    output.writelines("\nand it has minimum travel distance " + str(routeCosts.get(routeMap.endingNode).get("cost")) + "Km")
    output.writelines("\nit will take " + formattedTimeTaken + " minutes for the ambulance to reach the airport.")
    # print("'",routeCosts.get(routeMap.endingNode).get("path"),"'")
    # print("'"routeCosts.get(routeMap.endingNode).get("path")+"'")



main()

    



# =============================   TETST DATA  =============================#

# ******** Graph test Data ********

# g = Graph()
# g.addNode({"A": {"B": 3, "C": 1}})
# g.addNode({"B": {"A": 3, "C": 7, "D": 5}})
# g.addNode({"C": {"A": 1, "B": 7, "D": 2}})
# g.addNode({"D": {"B": 5, "C": 2, "E": 7}})
# g.addNode({"E": {"B": 1, "D": 7}})
# g.printGraph()
# print(g.getNodes())

# ********** Testing min heap priority queue with some sample data **********
# a = PriorityQueue()
# a.addNode('a', 20)
# a.addNode('b', 40)
# a.addNode('c',5)
# a.addNode('d',11)
# a.addNode('e',22)
# a.addNode('f',40)
# a.addNode('g',2)
# a.addNode('h',6)
# a.addNode('i',14)
# a.addNode('j',5)
# print("Min Element in the min heap = " ,a.getMinElement().value)
# a.printHeap()

# =============================   TETST DATA  =============================#