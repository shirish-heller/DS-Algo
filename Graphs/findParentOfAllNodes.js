class Graph {
    constructor(nodes, edges) {
        this.node = nodes;
        this.edges = edges;
    }
}

class Queue {
    constructor() {
        this.queue = [];
    }

    front() {
        return this.queue[0];
    }

     enqueue(val) {
        this.queue.push(val);
    }

    dequeue() {
        return this.queue.splice(0,1)[0];
    }

    isEmpty() {
        return this.queue.length==0 ? true: false;
    }

    printQueue() {
        console.log(this.queue);
    }
}

let nodes = ['A','B','C','D','F','G','H'];
let edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'G', 'H'],
    'D': ['B', 'F'],
    'F': ['D'],
    'G': ['C'],
    'H': ['C']
};

const findParentForAllNodes = (g)=> {
    let stack = [];
    let edges = g.edges;
    let startingNode = Object.keys(edges)[0];
    let parentMap = {[startingNode]: -1};
    stack.push(startingNode);
    while(stack.length>0) {
        let currentNode = stack.pop();
        let neighbours = edges[currentNode];
        for(let i=0; i<neighbours.length; i++) {
            if(!parentMap[neighbours[i]]) {
                parentMap[neighbours[i]] = currentNode;
                stack.push(neighbours[i]);
            }
        }
    }
    return parentMap;
}

let graph = new Graph(nodes, edges);
let result = findParentForAllNodes(graph);
console.log(result);