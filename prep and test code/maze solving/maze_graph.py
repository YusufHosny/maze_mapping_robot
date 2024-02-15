from enum import Enum
class Node:

    def __init__(self, edges: list = None, _name: str = "unnamed"):
        if edges is None:
            edges = []
        self.edges = edges

        # name purely for debugging purposes and possibly for mapping?
        self._name = _name

    def add_edge(self, _edge):
        if _edge not in self.edges:
            self.edges += [_edge]

    def __repr__(self) -> str:
        return f'n{self._name}'


class Edge:

    def __init__(self, _dir, _src: Node, _dst: Node):
        self.src = _src
        self.dst = _dst
        self.dir = _dir

# enumerator with relevant direcitons
class Directions(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def opposite(dir):
        if dir == Directions.UP:
            return Directions.DOWN
        elif dir == Directions.DOWN:
            return Directions.UP
        elif dir == Directions.LEFT:
            return Directions.RIGHT
        elif dir == Directions.RIGHT:
            return Directions.LEFT

class Orientation(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class Graph:

    def __init__(self):
        # initialize start node
        self.start = Node(_name = "1")
        self.nodes = [self.start]

    def add_node(self, src: Node, _dir: Node) -> Node:
        # if edge already exists return node without adding it
        for edge in src.edges:
            if edge.dir == _dir:
                return edge.dst

        # create new node and add to node list
        new_node = Node(_name = str(len(self.nodes) + 1))
        self.nodes += [new_node]

        # edge from source node to new node
        new_edge = Edge(_dir, src, new_node)
        src.add_edge(new_edge)

        # edge from new node to source node
        new_edge_inv = Edge(Directions.opposite(_dir), new_node, src)
        new_node.add_edge(new_edge_inv)

        # return new_node for further use
        return new_node


## currently a DFS pathfinder, for the purposes of this project its fine honestly
    def pathfind(self, start: Node, end: Node, _path: list = None, explored: list = None) -> list:
        # initialize empty path and explored lists if first call
        if _path is None:
            _path = []
        if explored is None:
            explored = []

        # add start node to explored
        explored += [start]

        # for each edge from start node
        for edge in start.edges:
            # copy path to current node
            path = _path[:]

            # node edge is going to
            next = edge.dst
                
            # if next hasn't been explored yet
            if next not in explored:
                # add path taken from start to next
                path += [edge.dir]

                # if reached end return the path
                if next == end:
                    return path

                # recursive pathfinding call
                new_path = self.pathfind(next, end, path, explored)

                # if a path was found return it
                if new_path is not None:
                    return new_path
        
        # if no path is found return None
        return None
    

    def get_xy_coordinates(self, node = None) -> tuple[int]:
        # if no node is passed, by default get start node
        if node is None:
            node = self.start

        # get all possible paths between current node and all other nodes
        paths = [self.pathfind(node, node_i) for node_i in self.nodes]
        # filter to non-None paths
        paths = [path for path in paths if path is not None]

        # get x and y coordinates, difference between times you moved left and right for the longest path
        # effectively gets the maximum number of times you can move left from the specified node
        x_pos = max([(path.count(Directions.LEFT) - path.count(Directions.RIGHT)) for path in paths], default=0)
        y_pos = max([(path.count(Directions.UP) - path.count(Directions.DOWN)) for path in paths], default=0)

        return x_pos, y_pos
    
    # get a node object from the graph via its x, y coordinates
    def get_node_at(self, x: int, y: int) -> Node:
        for node in self.nodes:
            if self.get_xy_coordinates(node) == (x, y):
                return node
    
    # get the dimensions of the graph
    def get_dims(self):
        dims = [0, 0]
        for node in self.nodes:
            coord = self.get_xy_coordinates(node)
            if coord[0] > dims[0]: dims[0] = coord[0]
            if coord[1] > dims[1]: dims[1] = coord[1]
        return [dims[0]+1, dims[1]+1]

    # EXPORT SECTION

    # gets the horizontal or vertical wall at a certain location
    # starting with top left as origin
    # e.g. horizonal(0, 0) = top left horizontal wall
    # vertical(max, max) bottom right vertical wall
    def check_wall_at(self, orientation , x: int, y: int):
        node = self.get_node_at(x, y)
        if orientation is Orientation.HORIZONTAL:
            return (Directions.UP in [edge.dir for edge in node.edges])
        elif orientation is Orientation.VERTICAL:
            return (Directions.LEFT in [edge.dir for edge in node.edges])
        
    

    # JSON return structure:
    # anonymous object, contains 2 attributes (horizontals and verticals) which each contains
    # a list of 0s and 1s defining whether there is or isnt a wall at a certain location
    # also contains an attribute dims which is a list of 2 elements defining the dimensions
    def json(self) -> str:
        # get dimensions
        dims = self.get_dims()
        json_dims = dims

        vert = []
        horz = []
        # populate wall arrays 
        for y in range(dims[1]):
            for x in range(dims[0]):
                vert += [0 if self.check_wall_at(Orientation.VERTICAL, x, y) else 1]
                horz += [0 if self.check_wall_at(Orientation.HORIZONTAL, x, y) else 1]
            vert += [1]
        horz += [1]*dims[0]
        
        json_string = f'{{\n\t"dims" : {json_dims},\n\t"verticals" : {vert},\n\t"horizontals" : {horz}\n}}'

        return json_string