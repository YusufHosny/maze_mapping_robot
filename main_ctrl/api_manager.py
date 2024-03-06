import requests
import json


# polling function
def poll_instructions():
    # call getInstruction until a non-empty list is returned
    while True:
        get_instruction = requests.get("https://studev.groept.be/api/a23ib2a03/getInstruction")
        json_obj = json.loads(get_instruction)
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
        requests.get(f"https://studev.groept.be/api/a23ib2a03/sendDataPacket/{position[0]}/{position[1]}/{json_maze}/1")
