import requests
import json


# polling function
def poll_instructions():
    # call getInstruction until a non-empty list is returned
    while True:
        get_instruction = requests.get("https://studev.groept.be/api/a23ib2a03/getInstruction")
        json_obj = get_instruction.json()
        if len(json_obj) > 0:
            return json_obj[0]["OpCode"]


# update functions
def set_instruction_complete():
    # call setInstructionComplete
    requests.get("https://studev.groept.be/api/a23ib2a03/setInstructionComplete")


def send_maze_packet(position=None, json_maze=None):
    # send empty packet to show "loading" if mapping incomplete
    # when mapping complete sends current position and maze json

    if position is None and json_maze is None:
        requests.get("https://studev.groept.be/api/a23ib2a03/sendEmptyDataPacket")
    else:
        requests.post(f"https://studev.groept.be/api/a23ib2a03/sendDataPacket/",
                      data={"px": position[0], "py": position[1], "map": json_maze, "completion": 1})



def rc_get():
    while True:
        get_rc_rq = requests.get("https://studev.groept.be/api/a23ib2a03/RC_get")
        json_obj = get_rc_rq.json()
        if len(json_obj) > 0:
            return json_obj[0]["rc_rq"]
        

def rc_set():
    # call setInstructionComplete
    requests.get("https://studev.groept.be/api/a23ib2a03/RC_complete")