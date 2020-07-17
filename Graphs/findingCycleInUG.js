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
    'A': ['B', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'G', 'H'],
    'D': ['A', 'B'],
    'F': ['A', 'D'],
    'G': ['C'],
    'H': ['C']
};

const findCycleInUG = (g)=> {
    let q = new Queue();
    let edges = g.edges;
    let startingNode = Object.keys(edges)[0];
    let output=[];
    let visited = {};
    q.enqueue(startingNode);
    while(!q.isEmpty()) {
        let currentNode = q.dequeue();
        visited[currentNode] = 1;
        let neighbours = edges[currentNode];
        for(let i=0; i<neighbours.length; i++) {
            if(!visited[neighbours[i]]) {
                q.enqueue(neighbours[i]);
                if(visited[neighbours[i]]==0) return true;
                else visited[neighbours[i]] = 0;
            }
        }
    }
    return false;
}

let graph = new Graph(nodes, edges);
let result = findCycleInUG(graph);
console.log(result);