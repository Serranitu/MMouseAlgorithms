import sys
from . import API
import numpy as np

def log(string):
    sys.stderr.write("{}\n".format(string))
    sys.stderr.flush()

def select(algorithm:str):
    log("Running...")
    API.setColor(0, 0, "G")
    API.setText(0, 0, "abc")
    if algorithm == 'left_wall':
        log("Selected Left Wall Algorithm")
        left_wall()

def left_wall():
    while True:
        if not API.wallLeft():
            API.turnLeft()
        while API.wallFront():
            API.turnRight()
        API.moveForward()