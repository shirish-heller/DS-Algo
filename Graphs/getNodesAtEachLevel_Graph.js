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

//get Nodes At Each Level in Graph
const getNodesAtEachLevel = (g)=> {
    let q = new Queue();
    let output = {};
    let edges = g.edges;
    let visited = {};
    let startingNode = Object.keys(edges)[0];
    q.enqueue(startingNode);
    currentLevel = 0;
    output[startingNode] = currentLevel;
    while(!q.isEmpty()) {
        let currentNode = q.dequeue();
        visited[currentNode] = true;
        let neighbours = edges[currentNode];
        currentLevel = output[currentNode] + 1;
        for(let i=0; i<neighbours.length; i++) {
            if(!visited[neighbours[i]]) {
                output[neighbours[i]] = currentLevel;
                // output[currentLevel] = !output[currentLevel] ? [currentNode] : [...output[currentLevel], currentNode];
                q.enqueue(neighbours[i]);
            }
        }
    }
    return output;
}

//*********************get Nodes At Each Level in Graph*******************//

let graph = new Graph(nodes, edges);
let result = getNodesAtEachLevel(graph);
console.log(result);

