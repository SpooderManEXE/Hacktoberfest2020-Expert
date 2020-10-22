class Graph {
    
    constructor(vertices = []) {
        this.vertices = vertices;
        this.connections = [];
    }

    addConnection(value1, value2) {
        if (this.connections.indexOf(value1) === -1) {
            this.connections[value1] = [];
        }
        this.connections[value1].push(value2);
    }

    getVerticeConnections(value) {
        return this.connections[value];
    }

    addVertice(vertice) {
        this.vertices.push(vertice)
    }
}

/**
 * Graph example usage
 * 
 * let graph = new Graph();
 * graph.addVertice(1);
 * graph.addVertice(2);
 * graph.addVertice(3);

 * graph.addConnection(1,2);
 * graph.addConnection(1,3);
 * console.log(graph.getVerticeConnections(1));
 */
