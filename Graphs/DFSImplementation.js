class Graph {
    constructor(nodes, edges) {
        this.node = nodes;
        this.edges = edges;
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

const dfs = (g)=> {
    let output = [];
    let edges = g.edges;
    let startingNode = Object.keys(edges)[0];
    const visit = (node)=> {
        if(output.indexOf(node)==-1) {
            output.push(node);
            let neighbours = edges[node];
            for(let i=0; i<neighbours.length; i++) {
                visit(neighbours[i], edges);
            }
        } else return;
    };
    visit(startingNode);
    return output;
}

console.log(dfs(graph));

