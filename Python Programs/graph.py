"""
A "graph"1 in mathematics and computer science consists of "nodes", also known as "vertices".
Nodes may or may not be connected with one another.
reference: https://www.python.org/doc/essays/graphs/
BASIC structure of graph:
    A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C
"""
from pprint import pprint


class Graph(object):
    def __init__(self, graph_dict=None, *args, **kwargs):
        # This(self.default_graph) is a dictionary whose keys are the nodes of the graph.
        # For each key, the corresponding value is a list containing the nodes
        # that are connected by a direct arc from this node
        if graph_dict:
            self.__default_graph = graph_dict
        else:
            # initializes a graph object  If no dictionary or None is given
            self.__default_graph = {'A': ['B', 'C'],
                                    'B': ['C', 'D'],
                                    'C': ['D'],
                                    'D': ['C'],
                                    'E': ['F'],
                                    'F': ['C']}

    def vertices(self, graph_dict=None):
        """
        find the vertices of a graph
        :param graph_dict: default graph will be used of graph_dict is not provided or is empty
        :return vertices of the graph
        """
        if not graph_dict:
            graph_dict = self.__default_graph
        return list(graph_dict.keys())

    def generate_edges(self, graph_dict=None):
        """
        Function to generate the list of all edges
        An edge can be seen as a 2-tuple with nodes as elements, i.e. ("a","b")
        :param graph_dict: graph for which edges to be found default graph will be used if no graph given
        :return: list of all edges of given graph
        """
        edges = []
        if not graph_dict:
            graph_dict = self.__default_graph
        for node in graph_dict:  # iterate over each node in graph (iterate on dictionary keys)
            for neighbour in graph_dict[node]:  # iterate over neighbouring nodes (values of corresponding key)
                edges.append((node, neighbour))  # add edge to list
        return edges

    def add_vertex(self, vertex, graph_dict=None):
        """
        If the vertex "vertex" is not in
        self.__default_graph, a key "vertex" with an empty
        list as a value is added to the dictionary.
        Otherwise nothing has to be done.
        :param vertex: vertex to be add in graph
        :param graph_dict: graph for which edges to be found default graph will be used if no graph given
        :return
        """
        if not graph_dict:
            graph_dict = self.__default_graph
        if vertex not in graph_dict:
            graph_dict[vertex] = []
        return graph_dict

    def vertex_degree(self, vertex, graph_dict=None):
        """
        The degree of a vertex v in a graph is the number of edges connecting it, with loops counted twice.
        The degree of a vertex is the number of edges connecting it,
        i.e. the number of adjacent vertices.
        Loops are counted double,
        i.e. every occurence of vertex in the list of adjacent vertices.

        The maximum degree of a graph G, denoted by Δ(G),
        and the minimum degree of a graph, denoted by δ(G), are the maximum and minimum degree of its vertices.
        """
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def find_isolated_nodes(self, graph_dict=None):
        """
        returns a list of isolated nodes (no edge containing the node )
        :param graph_dict: graph for which isolated nodes to be found default graph will be used if no graph given
        :return: list of all isolated nodes
        """
        isolated = []
        if not graph_dict:
            graph_dict = self.__default_graph
        for node in graph_dict:
            if not graph_dict[node]:
                isolated += node
        return isolated

    def find_min_degree(self, graph_dict=None):
        """ the minimum degree of the vertices """
        min_degree = 100000000
        if not graph_dict:
            graph_dict = self.__default_graph
        for vertex in graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min_degree:
                min_degree = vertex_degree
        return min_degree

    def find_max_degree(self, graph_dict=None):
        """ the maximum degree of the vertices """
        max_degree = 0
        if not graph_dict:
            graph_dict = self.__default_graph
        for vertex in graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max_degree:
                max_degree = vertex_degree
        return max_degree

    def find_path(self, graph, start, end, path=[]):
        """
        simple function to determine a path between two nodes
        algorithm paradigm: backtracking
        :param graph: graph
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
                    This argument is used to avoid cycles
        :return:a list of nodes (including the start and end nodes) comprising the path.
                When no path can be found, it returns None
        """
        path = path + [start]  # creates a new list.
        # If we had written "path.append(start)" instead,
        # we would have modified the variable 'path' in the caller
        if start == end:
            return path  # start and end node are same
        if start not in graph:
            return None  # graph does not contain given start node
        for node in graph[start]:  # explore nodes in corresponding start node
            if node not in path:  # If current node is unexplored then proceed ahead
                new_path = self.find_path(graph, node, end,
                                          path)  # find path from current node(as start node) to end node
                if new_path:
                    return new_path  # if new_path found between nodes then return the new_path
        return None  # no path can be found, returns None

    def find_all_paths(self, graph, start, end, path=[]):
        """
        find all paths from one node to other in given graph
        :param graph: graph structure
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
        :return: all explored paths
        """
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []  # maintain a list to store all explored path
        for node in graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(graph, node, end, path)
                for new_path in new_paths:
                    paths.append(new_path)  # add new path to list instead of returning it.
        return paths

    def find_shortest_path(self, graph, start, end, path=[]):
        """
        find shortest path from one node to other in given graph
        :param graph: graph structure
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
        :return: shortest path between two nodes
        """

        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None  # maintain a variable to check with every new explored path, replace existing with shortest one
        for node in graph[start]:
            if node not in path:
                new_path = self.find_shortest_path(graph, node, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest


if __name__ == "__main__":
    graph_obj = Graph()  # Graph object
    # construct a basic graph
    my_graph = {'A': ['B', 'C'],
                'B': ['C', 'D'],
                'C': ['D'],
                'D': ['C'],
                'E': ['F'],
                'F': ['C']}
    print("Input graph-")
    pprint(my_graph)  # print input graph
    # find path
    print("Get path from start to end nodes: {}".format(graph_obj.find_path(my_graph, 'A', 'D')))
    # find all path
    print("All paths from start to end node: {}".format(graph_obj.find_all_paths(my_graph, 'A', 'D')))
    # find shortest path
    print("Get Shortest paths from start to end node: {}".format(graph_obj.find_shortest_path(my_graph, 'A', 'D')))
