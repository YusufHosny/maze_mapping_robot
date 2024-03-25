from mapper import Mapper
from time import sleep
import api_manager as api
from robot import robot_controller


# INITIALIZATION
m = Mapper()
r = robot_controller(0.5, 0.01, 1, 0.32)
m.check_around = r.check_sensors
m.move_to = r.move_to

# while True:
#     r.read_sensors(1)

# MAIN LOOP
while True:
    # start API polling function, polls and returns when new instruction is received
    instruction = api.poll_instructions()

    # process and execute instructon
    # Moving (X, Y)
    if instruction[:3] == "MOV":
        print("moving...", end='')
        # get argument
        grid_pos = (int(instruction[4]), int(instruction[6]))
        # move to target node
        m.go_to_node(m.maze.get_node_at(grid_pos[0], grid_pos[1]))

    # Mapping
    if instruction == "MAP" and m.is_mapped == False:
        print("mapping...", end='')
        m.map()

    if instruction == "MNL":
        print("manual control mode. use wasd.")
        r.manual()

    if instruction == "RST":
        print("reseting...", end='')
        m = Mapper()
        m.check_around = r.check_sensors
        m.move_to = r.move_to

    print("Done")
    # update instruction as complete on API
    api.set_instruction_complete()

    # sleep between checks to allow API error tolerace
    sleep(1)
    
