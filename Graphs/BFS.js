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
let graph = new Graph(nodes, edges);
console.log(bfs(graph));

//BFS ALGO
const bfs = (g)=> {
    let q = new Queue();
    let output = [];
    let edges = g.edges;
    let startingNode = Object.keys(edges)[0];
    const visit = (node)=> {
        if(output.indexOf(node)==-1) {
            output.push(node);
            let neighbours = edges[node];
            for(let i=0; i<neighbours.length; i++) {
                if(output.indexOf(neighbours[i])==-1) {
                    q.enqueue(neighbours[i]);
                }
            }
            if(!q.isEmpty()) visit(q.dequeue());
            else return;
        }
    };
    visit(startingNode);
    return output;
}

