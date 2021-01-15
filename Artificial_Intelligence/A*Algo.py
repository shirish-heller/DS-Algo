from PriorityQueue import PriorityQueue
from Graph import Graph

def searchWithAStar(graph, goalNode):
    priorityQueue = PriorityQueue()
    priorityQueue.addNode((graph.nodes[0],0,0))
    visitedNodes = []
    while(priorityQueue.isEmpty()==False):
        node = priorityQueue.pop()
        lastNodeInCurrentPath = node[0][-1]
        if(lastNodeInCurrentPath == goalNode):
            print("Reached the Goal!!!\n")
            print("optimal path = ", node[0])
            print("PathCost = ", node[2])
            return
        if(lastNodeInCurrentPath not in visitedNodes):
            # Adding children on current Node to PQ
            childNodes = graph.edges.get(lastNodeInCurrentPath)
            if(childNodes):
                for currNode in childNodes:
                    path = node[0] + currNode[0]
                    priorityQueue.addNode((path, node[2]+currNode[1]+heuristics[currNode[0]], node[2]+currNode[1]))

        # Adding visited Node to visited Arr
        visitedNodes.append(lastNodeInCurrentPath)

nodes = ['S', 'B', 'C', 'D', 'E', 'F', 'G']
edges = {
    'S': [('B',4), ('C',3)],
    'B': [('E',12)],
    'C': [('D',7), ('E',10)],
    'D': [('E',2)],
    'E': [('G',5)],
    'F': [('G',16)],
    'G': []
    }

heuristics = {
    'S':14,
    'B':12,
    'C':11,
    'D':6,
    'E':4,
    'F':11,
    'G':0
}

graph = Graph(nodes, edges)
searchWithAStar(graph, 'G')