from maze_graph import Directions, Node, Graph as Maze

class Mapper:
    
    def __init__(self) -> None:
        self.maze = Maze()
        self.cur_node = self.maze.start
        self.unmapped_nodes = []
        self.mapped_nodes = set()
        self.is_mapped = False

    # tuple of 4 booleans indicating if theres a path (True) or wall (False) in each direction
    def check_around(self) -> tuple[bool]:
        return self._check_around_input()
        # TODO check around with sensors and return if theres a wall or not for each dir

    
    def go_to_node(self, node: Node):
        self._go_to_node_simulate(node)
        # TODO move physically with motors to node

    # SIMULATION: instead of using sensors, input positions
    def _check_around_input(self) -> tuple[bool]:
        inp = input("Input current surroundings: ")
        out = ()
        for letter in inp:
            if letter == "1": out += (True,)
            else: out += (False,)
        
        return out

    # SIMULATION: instead of moving, print the path taken
    def _go_to_node_simulate(self, node: Node):
        path = self.maze.pathfind(self.cur_node, node)
        for dir in path: print(dir) 


    def map_node(self):
        # add to mapped nodes
        self.mapped_nodes.add(self.cur_node)

        # check surroundings
        surroundings = self.check_around()

        ## Add edges and nodes based on surroundings
        # up
        if surroundings[0]:
            node_found = self.maze.add_node(self.cur_node, Directions.UP)
            if node_found not in self.unmapped_nodes and node_found not in self.mapped_nodes:
                self.unmapped_nodes.insert(0, node_found)

        # down
        if surroundings[1]:
            node_found = self.maze.add_node(self.cur_node, Directions.DOWN)
            if node_found not in self.unmapped_nodes and node_found not in self.mapped_nodes:
                self.unmapped_nodes.insert(0, node_found)

        # left
        if surroundings[2]:
            node_found = self.maze.add_node(self.cur_node, Directions.LEFT)
            if node_found not in self.unmapped_nodes and node_found not in self.mapped_nodes:
                self.unmapped_nodes.insert(0, node_found)

        # right
        if surroundings[3]:
            node_found = self.maze.add_node(self.cur_node, Directions.RIGHT)
            if node_found not in self.unmapped_nodes and node_found not in self.mapped_nodes:
                self.unmapped_nodes.insert(0, node_found)


    def map(self):
        self.map_node()
        # while there are still unmapped nodes
        while len(self.unmapped_nodes) > 0:
            # go to the first node in the unmapped node list
            next = self.unmapped_nodes[0]
            self.go_to_node(next)

            # set it as the current node and map it
            self.cur_node = next
            self.map_node()

            # remove it from the list of unmapped nodes
            self.unmapped_nodes.remove(next)
            
        self.is_mapped = True





