import keyboard
import requests
import time

URL = "https://studev.groept.be/api/a23ib2a03/RC_send/"
stopped = False

while True:
    if keyboard.is_pressed("w"):
        requests.get(URL + "forward")
        stopped = False
    elif keyboard.is_pressed("a"):
        requests.get(URL + "left")
        stopped = False
    elif keyboard.is_pressed("d"):
        requests.get(URL + "right")
        stopped = False
    elif not stopped:
        requests.get(URL + "stop")
        stopped = True
    time.sleep(0.1)