from mapper import Mapper
from time import sleep


# INITIALIZATION
m = Mapper()


# MAIN LOOP
while True:
    # start API polling function, polls and returns when new instruction is received
    instruction = 0 # TODO add polling

    # process and execute instructon
    # Moving (X, Y)
    if instruction[:3] == "MOV":
        # get argument
        grid_pos = (instruction[4], instruction[6])
        # move to target node
        m.go_to_node(m.maze.get_node_at(grid_pos[0], grid_pos[1]))

    # Mapping
    if instruction == "MAP" and m.is_mapped == False:
        m.map()

    # update instruction as complete on API


    # sleep between checks to allow API error tolerace
    sleep(1)
    
